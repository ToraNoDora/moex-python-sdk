"""Это основной пакет модуля"""

import logging
import urllib3

from typing import List, Optional

import pandas as pd

from requests import Session
from requests.auth import HTTPProxyAuth

from moex_python_sdk.api import MoexApi
from moex_python_sdk.api._api import BaseApi
from moex_python_sdk.models import MoexProxy


class Moex:
    """https://iss.moex.com"""

    def __init__(self, base_url: str, verify: Optional[str] = False, warnings: bool = True):
        logging.basicConfig(
            format="[%(asctime)s] - %(message)s",
            datefmt="%d-%b-%y %H:%M:%S",
            level=logging.INFO,
        )

        self._url = f"{base_url}/iss"
        self._session = Session()
        self._api = BaseApi(
            base_url=self._url,
            session=self._session,
            verify=verify,
            warnings=warnings,
        )
        self._prepare_srv()

    def _prepare_srv(self):
        self._moex_api = MoexApi(self._api)

    # def authorize(self, login: str, password: str):
    #     """Запустить авторизацию с указанным логином и паролем. Вне зависимости от
    #     успеха авторизации вернется объект :py:class:`requests.Response`"""

    #     r = self._api.post(
    #         "/authorizate",
    #         json={"login": login, "pass": password},
    #         headers={
    #             "Authorization": "Basic OXVESTh4YTU6V1NIOHNQQ0JQTktZR2lHcml6Rmtnb3A="
    #         },
    #         as_json=False,
    #     )

    #     # TODO check errors before accessing token, There can be wrong login | password
    #     # error, we should raise an exception here

    #     print(r.json())
    #     self._api.update_access_token(r.json()["data"]["success"]["access_token"])
    #     return r

    def auth_proxy(self, proxy: MoexProxy):
        auth = HTTPProxyAuth(proxy.user.username, proxy.user.password)
        self._session.proxies = proxy.proxies.model_dump(exclude_none=True)
        self._session.auth = auth

    def api(self) -> MoexApi:
        return self._moex_api

    def logging_on(self):
        import http.client

        http.client.HTTPConnection.debuglevel = 1

        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)

        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True


def df_data(columns: List, data: List) -> pd.DataFrame:
    return pd.DataFrame(data, columns=columns)

