import pytest
from mixer.backend.django import mixer

from api.models import CADRecord
from api.tasks.utils import CADModelSyncService
from api.tests.service_mock_data import instances_by_des


class TestSyncService:

    service = CADModelSyncService()

    def test_associate_returns_dict(self):
        data = {
            'fields': ['A', 'B', 'C'],
            'data': [[1, 2, 3], [3, 4, 5]]
        }
        compiled_dict = self.service.associate_fields(data)
        expected = [{'A': 1, 'B': 2, 'C': 3}, {'A': 3, 'B': 4, 'C': 5}]

        assert compiled_dict == expected

    @pytest.mark.parametrize('instance_des, expected', [
        ('2016 DY30', 5),
        ('2019 AC3', 7)
    ])
    def test_update_multiple_instances(
            self, db, instance_des, expected
    ):
        intersection = {'2016 DY30', '2019 AC3'}
        instance = mixer.blend(CADRecord, des=instance_des)
        self.service._update_instances(
            intersection,
            instances_by_des,
            CADRecord
        )
        updated_instance = CADRecord.objects.get(
            pk=instance.pk
        )

        assert updated_instance.orbit_id == expected

    def test_update_single_instance_fields(self, db):
        instance = mixer.blend(CADRecord, des='2016 DY30')
        self.service._update_fields(
            instances_by_des,
            instance,
            CADRecord
        )
        updated_instance = CADRecord.objects.get(
            pk=instance.pk
        )
        expected = 5
        assert updated_instance.orbit_id == expected