"""Это основной пакет модуля"""

import logging
import urllib3

from requests import Session
from requests.auth import HTTPProxyAuth

from moex_python_sdk.api import MoexApi
from moex_python_sdk.api._api import BaseApi
from moex_python_sdk.df import MoexDataframe
from moex_python_sdk.models import MoexProxy


class Moex:
    """https://iss.moex.com/iss"""

    def __init__(self, base_url: str):
        urllib3.disable_warnings() # ssl warnings
        logging.basicConfig(
            format="[%(asctime)s] - %(message)s",
            datefmt="%d-%b-%y %H:%M:%S",
            level=logging.INFO,
        )
        self.url = f"{base_url}/iss"

        self._session = Session()
        self._api = BaseApi(self.url, self._session)
        self._moex_api = MoexApi(self._api)

        self._prepare_srv()

    def _prepare_srv(self):
        self._dataframe_srv = MoexDataframe(self._moex_api)

    def auth_proxy(self, proxy: MoexProxy):
        auth = HTTPProxyAuth(proxy.user.username, proxy.user.password)
        self._session.proxies = proxy.proxies.dict(exclude_none=True)
        self._session.auth = auth # Set authorization parameters globally

    def api(self) -> MoexApi:
        return self._moex_api
    
    # ======   srv   ======
    def df(self) -> MoexDataframe:
        return self._dataframe_srv
    
    # ====== END srv ======

    def logging_on(self):
        import http.client

        http.client.HTTPConnection.debuglevel = 1

        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)

        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True

