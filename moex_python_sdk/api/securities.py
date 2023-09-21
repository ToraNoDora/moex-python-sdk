from moex_python_sdk.api._api import BaseApi
from moex_python_sdk.decorators import resp

from moex_python_sdk.models import new_resp_data
from moex_python_sdk.models.securities import (
    SecuritiesParams,
    Securities,
    SecurityParams,
    Security,
    SecurityIndicesParams,
    SecurityIndices,
    SecurityAggregatesParams,
    SecurityAggregates,
)


@resp
class SecurityApi:
    def __init__(self, api: BaseApi):
        self.api = api
        self.endpoint = "/securities"

    def get_securities(self, params: SecuritiesParams, format: str = "json"):
        """Список бумаг торгуемых на московской бирже."""

        r = self.api.get(
            f"{self.endpoint}.{format}",
            params=params.as_dict(),
        )

        return r["url"], Securities(securities=new_resp_data(r["data"]["securities"]))

    def get_security(self, security: str, params: SecurityParams, format: str = "json"):
        """Получить спецификацию инструмента. Например: https://iss.moex.com/iss/securities/IMOEX.xml."""

        r = self.api.get(
            f"{self.endpoint}/{security}.{format}",
            params=params.as_dict(),
        )

        return r["url"], Security(
            description=new_resp_data(r["data"]["description"]),
            boards=new_resp_data(r["data"]["boards"]),
        )

    def get_security_indices(self, security: str, params: SecurityIndicesParams, format: str = "json"):
        """Список индексов в которые входит бумага."""

        r = self.api.get(
            f"{self.endpoint}/{security}/indices.{format}",
            params=params.as_dict(),
        )

        return r["url"], SecurityIndices(indices=new_resp_data(r["data"]["indices"]))

    def get_security_aggregates(self, security: str, params: SecurityAggregatesParams, format: str = "json"):
        """Агрегированные итоги торгов за дату по рынкам."""

        r = self.api.get(
            f"{self.endpoint}/{security}/aggregates.{format}",
            params=params.as_dict(),
        )

        return r["url"], SecurityAggregates(
            aggregates=new_resp_data(r["data"]["aggregates"]),
            agregates_dates=new_resp_data(r["data"]["agregates.dates"]),
        )
