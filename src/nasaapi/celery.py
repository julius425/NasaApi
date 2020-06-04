import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')

app = Celery('nasaapi')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

"""
start schedule
celery -A shlconnector worker -B -l info
"""

app.conf.beat_schedule = {
    # sf_api tasks
    'sync_requisitions_task': {
        'task': 'api.tasks.tasks.sync_cad_data',
        'schedule': crontab(minute='*/30'),
    },
}