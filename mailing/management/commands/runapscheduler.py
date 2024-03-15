import logging

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore

from mailing.utils import send_ready_mailings

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    При запуске этот робот проверяет список рассылки каждые 10 секунд и отправляет всё готовое к рассылке и в соответствующее время.
    """

    def handle(self, *args, **options):
        print('apscheduler work')
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            send_ready_mailings,
            trigger=CronTrigger(second="*/10"),  # Каждые 10 секун
            id="send_ready_mailings",  # Идентификатор, присвоенный каждому заданию, ДОЛЖЕН быть уникальным.
            max_instances=1,
            replace_existing=True,
        )

        try:
            logger.info("Запуск планировщика...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Остановка планировщика...")
            scheduler.shutdown()
            logger.info("Планировщик успешно закрылся!")
