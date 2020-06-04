import pytest

from api.connector import NasaApiSession
from api.tests.connector_mock_data import cad_mock_data


class TestSession:

    session = NasaApiSession()

    def test_nasa_api_connection(self):
        response = self.session.test_connection()
        assert response.status_code == 200

    @pytest.mark.parametrize('data, method', [
        (cad_mock_data, 'request_cad_data'),
        (cad_mock_data, 'request_fireball_data'),
    ])
    def test_method_collects_valid_data(self, mocker, data, method):
        mocker.patch(
            f'api.connector.NasaApiSession.{method}',
            return_value=data
        )
        result = self.session.request_cad_data()
        result = result['data']
        assert isinstance(result, list)

