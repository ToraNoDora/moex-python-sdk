from moex_python_sdk.api._api import BaseApi
from moex_python_sdk.decorators import resp

from moex_python_sdk.models import new_resp_data
from moex_python_sdk.models.analytical_products import (
    CurvesParams,
    Curves,
    CurvesSecurityParams,
    FutoiParams,
    Futoi,
    FutoiSecurityParams,
    Netflow2Params,
    Netflow2,
    Netflow2SecurityParams,
)


@resp
class AnalyticalProductApi:
    def __init__(self, api: BaseApi):
        self.api = api
        self.endpoint = "/analyticalproducts"

    def get_curves_securities(self, params: CurvesParams, format: str = "json"):
        """Будущие ставки для ценообразования нестандартных инструментов (деривативов)."""

        r = self.api.get(
            f"{self.endpoint}/curves/securities.{format}",
            params=params.as_dict(),
        )

        return r["url"], Curves(curves=new_resp_data(r["data"]["curves"]))

    def get_curves_security(self, security: str, params: CurvesSecurityParams, format: str = "json"):
        """Будущие ставки для ценообразования нестандартных инструментов (деривативов)."""

        r = self.api.get(
            f"{self.endpoint}/curves/securities/{security}.{format}",
            params=params.as_dict(check=True),
        )

        return r["url"], Curves(curves=new_resp_data(r["data"]["curves"]))

    def get_futoi_securities(self, params: FutoiParams, format: str = "json"):
        r = self.api.get(
            f"{self.endpoint}/futoi/securities.{format}",
            params=params.as_dict(),
        )

        return r["url"], Futoi(
            futoi=new_resp_data(r["data"]["futoi"]),
            futoi_dates=new_resp_data(r["data"]["futoi.dates"]),
        )

    def get_futoi_security(self, security: str, params: FutoiSecurityParams, format: str = "json"):
        r = self.api.get(
            f"{self.endpoint}/futoi/securities/{security}.{format}",
            params=params.as_dict(check=True),
        )

        return r["url"], Futoi(
            futoi=new_resp_data(r["data"]["futoi"]),
            futoi_dates=new_resp_data(r["data"]["futoi.dates"]),
        )

    def get_netflow2_securities(self, params: Netflow2Params, format: str = "json"):
        r = self.api.get(
            f"{self.endpoint}/netflow2/securities.{format}",
            params=params.as_dict(),
        )

        return r["url"], Netflow2(netflow2=new_resp_data(r["data"]["netflow2"]))

    def get_netflow2_security(self, security: str, params: Netflow2SecurityParams, format: str = "json"):
        """
        Дата в формате YYYY-MM-DD начиная с которой отдаются данные.

        Обратите внимание, что для данного запроса нет постраничной навигации.
        вам необходимо будет изменять параметр &from на дату следующую после полученных вами данных.
        Количество отдаваемых записей в одном блоке ограничено 1000.

        till
        Дата в формате YYYY-MM-DD которой будет заканчиваться интервал.
        Данный параметр должен быть больше или равен параметру till.
        """

        r = self.api.get(
            f"{self.endpoint}/netflow2/securities/{security}.{format}",
            params=params.as_dict(check=True),
        )

        return r["url"], Netflow2(netflow2=new_resp_data(r["data"]["netflow2"]))

