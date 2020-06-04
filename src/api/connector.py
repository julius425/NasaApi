import requests
import typing as t
from json import JSONDecodeError
from urllib.parse import urlencode
from requests.auth import HTTPBasicAuth

from django.conf import settings

from utils.types import TJsonDict, TJsonList


class NasaApiBaseSession:
    """Base session

    Provides url list and basic request methods
    to NASA API.
    """
    BASE_URL = settings.NASA_BASE_URL
    CAD_URL = f'{BASE_URL}/cad.api'
    FIREBALL_URL = f'{BASE_URL}/fireball.api'
    MD_URL = f'{BASE_URL}/mdesign.api'
    NHATS_URL = f'{BASE_URL}/nhats.api'
    SBDB_URL = f'{BASE_URL}/sbdb.api'
    SCOUT_URL = f'{BASE_URL}/scout.api'
    SENTRY_URL = f'{BASE_URL}/sentry.api'

    def __init__(self):
        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth(
            'api_key', settings.NASA_API_KEY
        )
        self.session.headers.update({
            'Accept': 'application/json',
            'Content-Type': 'application/json;charset=utf-8'
        })

    @staticmethod
    def url(url: str, params: t.Dict[str, t.Any]) -> str:
        return f'{url}/?{urlencode(params)}'

    def test_connection(self):
        return self.session.get(
            self.BASE_URL
        )

    def get_request(
            self, url: str, detail: bool = False
    ) -> t.Union[TJsonDict, TJsonList]:
        """GET request data

        detail for single object
        """
        try:
            response = self.session.get(url)
            result = response.json()
            return result
        except JSONDecodeError as e:
            raise e
        except ConnectionError as e:
            raise e


class NasaApiSession(NasaApiBaseSession):
    """Extended session

    Provides methods to request specific data from NASA API.
    """

    def request_cad_data(self, params: t.Dict={}) -> TJsonDict:
        """Close Approaches Data

        Asteroid and comet close approaches to the planets
        in the past and future
        """
        url = self.url(f"{self.CAD_URL}", params)
        return self.get_request(url)

    def request_fireball_data(self, params: t.Dict={}) -> TJsonDict:
        """Fireball

        Fireball atmospheric impact data reported by
        US Government sensors.
        """
        url = self.url(f"{self.FIREBALL_URL}", params)
        return self.get_request(url)

    def request_md_data(self, params: t.Dict={}) -> TJsonDict:
        """Mission Design

        This API provides access to the JPL/SSD
        small-body mission design suite.

        require params:
        """
        url = self.url(f"{self.MD_URL}", params)
        return self.get_request(url)

    def request_nhats_data(self, params: t.Dict={}) -> TJsonDict:
        """Near-Earth Object Human Space Flight Accessible Targets Study

        The NHATS API provides a method of requesting data
        from the NHATS-related tables in the SBDB
        """
        url = self.url(f"{self.NHATS_URL}", params)
        return self.get_request(url)

    def request_sbdb_data(self, params: t.Dict={}) -> TJsonDict:
        """Small-Body DataBase

        The SBDB API provides a method
        of requesting machine-readable data for a specified
        small body within JPL’s SSD/CNEOS Small-Body DataBase (SBDB).

        require params:
        """
        url = self.url(f"{self.SBDB_URL}", params)
        return self.get_request(url)

    def request_scout_data(self, params: t.Dict = {}) -> TJsonDict:
        """Scout

        This API provides access to near-realtime results
        from the CNEOS Scout system.
        """
        url = self.url(f"{self.SCOUT_URL}", params)
        return self.get_request(url)

    def request_sentry_data(self, params: t.Dict = {}) -> TJsonDict:
        """Sentry

        This API provides access to results from the
        CNEOS Sentry system.
        """
        url = self.url(f"{self.SCOUT_URL}", params)
        return self.get_request(url)

