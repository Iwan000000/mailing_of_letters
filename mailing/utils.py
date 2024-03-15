import datetime
from datetime import timedelta

import pytz
from django.core.mail import send_mail

from client.models import Client
from config.settings import EMAIL_HOST_USER
from log.models import Log
from mailing.models import Mailing
from message.models import Message


def check_status_mailing(mailing):
    """
    Эта функция для проверки статуса рассылки. Если все ок - измените Статус на Готово.
    """
    if mailing.status != 'Закончить':
        if len(Message.objects.filter(mailing=mailing.pk).all()) > 0:
            if len(Client.objects.filter(mailing=mailing.pk).all()) > 0:
                return 'Готов'
            else:
                return 'Не готов'
        else:
            return 'Не готов'
    else:
        return 'Закончить'


def mailing_execution(mailing):
    """
    Эта функция для выполнения рассылки.
    """
    if check_date_mailing_finish(mailing):
        mailing = Mailing.objects.get(pk=mailing.pk)
        message = Message.objects.get(mailing=mailing.pk)
        clients = Client.objects.filter(mailing=mailing.pk).all()
        answers = []
        success_attempt = 0
        unsuccessful_attempt = 0
        for client in clients:
            try:
                print('хост электронной почты')
                print(EMAIL_HOST_USER)
                print('конечный хост электронной почты')
                answer = send_mail(
                    subject=message.title,
                    message=get_letter(client, message),
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[client.email]
                )
                answers.append(
                    f'Почтовое отправление - {mailing.name}, Дата - {datetime.datetime.now()}, {client.email} - {answer}/n')
                success_attempt += 1
            except Exception:
                print('Ошибка')
                answers.append(
                    f'Почтовое отправление - {mailing.name}, Дата - {datetime.datetime.now()}, {client.email} - Ошибка/n')
                unsuccessful_attempt += 1
        add_history_of_mailing(mailing, answers, success_attempt, unsuccessful_attempt)
        if success_attempt > 0:
            add_new_datetime(mailing)
    else:
        mailing.status = 'Закончить'
        mailing.save()


def add_new_datetime(mailing):
    """
    Если рассылка повторяется, то эта функция устанавливает новое вре.
    """
    if mailing.periodicity_id == 1:
        mailing.status = 'Закончить'
    elif mailing.periodicity_id == 2:
        mailing.data_mailing = datetime.datetime.now() + timedelta(days=1)
    elif mailing.periodicity_id == 3:
        mailing.data_mailing = datetime.datetime.now() + timedelta(days=7)
    if check_date_mailing_finish(mailing):
        mailing.status = 'Закончить'
    mailing.save()


def add_history_of_mailing(mailing, answers, success_attempt, unsuccessful_attempt):
    """
    Эта функция для добавления истории об отправке в журнал рассылок.
    """
    new_log = {
        "datatime": datetime.datetime.now(),
        "mailing": mailing,
        "status": f"Success - {success_attempt}, Unsuccessful - {unsuccessful_attempt}",
        "answer_mail_server": answers,
    }
    Log.objects.create(**new_log)


def send_ready_mailings():
    """
    Эта функция находит рассылку со статусом Готово и датой окончания срока действия. И начните отправлять сообщения клиентам
    (если такие рассылки были найдены).
    """
    utc = pytz.UTC
    now = datetime.datetime.now().replace(tzinfo=utc)
    mailings = Mailing.objects.filter(status='Готов').all()
    count = 0
    for mailing in mailings:
        datetime_mailing = mailing.data_mailing.replace(tzinfo=utc)
        if now > datetime_mailing:
            if check_date_mailing_finish(mailing):
                mailing_execution(mailing.pk)
                count += 1
            else:
                mailing.status = 'Закончить'
                mailing.save()
    if count > 0:
        print(f'Все рассылки со статусом Готово завершены. Общий {count} рассылки.')
    else:
        print('Я не нашел рассылок со статусом Готово. Попробую в ближайшее время...')


def sorting_list_mailings(mailings_list):
    """
    Функция сортировки рассылок. return: контекст со списком рассылки и списком завершения
    """
    finished_list = []
    result_list = []
    if len(mailings_list) > 0:
        for mailing in mailings_list:
            result = {
                "mailing": mailing,
                "message": Message.objects.filter(mailing=mailing).last(),
                "number_of_clients": len(Client.objects.filter(mailing=mailing).all()),
                "number_of_times": len(Log.objects.filter(mailing=mailing).all()),
                "last_time": Log.objects.filter(mailing=mailing).last(),
            }
            if mailing.status == 'Готов':
                result['готов'] = True
            if mailing.status in ['Закончить', 'Отменить']:
                finished_list.append(result)
            else:
                result_list.append(result)
    context = {
        "mailing_list": result_list,
        "finished_list": finished_list,
    }
    if len(finished_list) > 0:
        context["number_finished_mailings"] = len(finished_list)
    else:
        context["number_finished_mailings"] = False
    return context


def get_letter(client, message):
    """
    Функция создания письма для клиента.
    """
    result = f'Привет {client.name} {client.lastname},/n{message.body}'
    return result


def check_date_mailing_finish(mailing):
    if mailing.data_mailing_finish:
        utc = pytz.UTC
        now = datetime.datetime.now().replace(tzinfo=utc)
        if mailing.data_mailing_finish > now:
            return True
        else:
            return False
    else:
        return True
