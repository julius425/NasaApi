import pytest
import mixer

from api.models.cad import CADRecord


@pytest.fixture
def cad_record(db):
    return mixer.blend(CADRecord)

