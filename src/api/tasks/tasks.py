from nasaapi.celery import app

from api.connector import NasaApiSession
from api.models.cad import CADRecord
from api.tasks.utils import CADModelSyncService


@app.task()
def sync_cad_data():
    """
    Synchronise data from api
    """
    session = NasaApiSession()
    service = CADModelSyncService()
    cad_data = session.request_cad_data()
    associated_cad_data = service.associate_fields(cad_data)
    service.sync_instances(associated_cad_data, CADRecord)
