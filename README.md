# Почтовый сервис

## Описание
Программа рассылки позволяет пользователям создавать и отправлять почтовые рассылки различным группам клиентов. Рассылка может содержать информацию, предложения или объявления, которые необходимо доставить выбранным получателям.
Основными функциональными возможностями программы рассылки являются:
1. Создание новых рассылок: Пользователи могут создавать новые рассылки, указывая название, содержание и периодичность отправления.
2. Управление получателями: Пользователи могут добавлять и удалять клиентов из групп получателей, чтобы определить, кому будет отправлена конкретная рассылка.
3. Планирование отправки: Пользователи могут запланировать отправку рассылки на определенное время и дату или отправить ее немедленно.
4. Отслеживание результатов: После отправки рассылки пользователи могут отслеживать результаты доставки, такие как количество отправленных, прочитанных или отклоненных писем.
5. Отчеты и аналитика: Программа предоставляет отчеты и аналитическую информацию о прогрессе и эффективности рассылок, позволяя пользователям оценить успех своих кампаний и внести коррективы в будущих рассылках.

Программа рассылки обладает простым и удобным пользовательским интерфейсом, что позволяет пользователям легко создавать и отправлять рассылки без необходимости в специализированных знаниях или навыках программирования. Она может быть использована для различных целей, таких как маркетинговые кампании, информационные бюллетени, приглашения на мероприятия и многое другое.

Программа рассылки представляет собой мощный инструмент для организации и управления эффективными почтовыми рассылками, помогая пользователям достигать своих целей и улучшать коммуникацию со своими клиентами.

## Установка
Сначала установите проект с GitHub
установка зависимостей

pip -r requirements.txt




## Подключение к базе данных
Затем создайте базу данных PosgreSQL. 

СОЗДАТЬ БАЗУ ДАННЫХ mailings
Затем необходимо подключить сервис к базе данных. Вам необходимо указать параметры базы данных в файле "config/settings.py" (например, имя пользователя и пароль).

Затем вы должны выполнить миграцию с помощью этих команд
python manage.py makemigrations
Если все в порядке, то
python manage.py мигрировать


## Переменные окружения
Для работы почтового сервиса необходимо создать файл ".env" с информацией о вашем почтовом сервисе и прочем. Пример этот файл вы можете увидеть как ".env.sample"
```
EMAIL_HOST=
ЭЛЕКТРОННАЯ ПОЧТА=
ПАРОЛЬ ЭЛЕКТРОННОЙ ПОЧТЫ=
CACHE_ENABLED=
МЕСТОПОЛОЖЕНИЕ КЭША=
```

## Создание суперпользователя
Для создания суперпользователя вам следует использовать команду
``
python manage.py csu
```

## Группа штатных пользователей
Для штатных пользователей есть две группы - **Модератор** и **Контент-менеджер**.
Только суперпользователь может добавить разрешение в админ-панели.

## Возможности модератора
Модератор может просматривать все рассылки и пользователей. Модератор может отменять и активировать все рассылки. Модератор может деактивировать и активировать всех пользователей. Модератор не может изменять и удалять рассылки.

## Возможности контент-менеджера
Контент-менеджер может добавлять и изменять статьи.

## Расписание запуска
Для запуска автоматической отправки рассылок вам следует использовать команду. Apscheduler просматривает все рассылки, проверяет, какие рассылки следует отправить, и отправляет. Эта проверка происходит каждые 10 секунд.
``
python manage.py runapscheduler
```

## Другие команды
Для разовой отправки всех готовых рассылок вам следует использовать команду
```
python manage.py запуск рассылок