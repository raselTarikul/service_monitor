from .base import *

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'service_monitor',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Celery settings
CELERY_BROKER_URL = "amqp://localhost"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Singapore' 
CELERY_BEAT_SCHEDULE = {
 'task-monitor': {
       'task': 'monitor_urls_task',
        # There are 4 ways we can handle time, read further 
       'schedule': 10.0,
    }     
}

CSV_PATH = '/csv'
