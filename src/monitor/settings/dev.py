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


# Celery settings
CELERY_BROKER_URL = "amqp://localhost"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Singapore' 

# Celert beat to run the task every 10 minuts
CELERY_BEAT_SCHEDULE = {
 'task-monitor': {
       'task': 'monitor_urls_task',
       'schedule': 600.0,
    }     
}

# path for the csv file
CSV_PATH = '/csv/'
