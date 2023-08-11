from moex_python_sdk.api._api import BaseApi
from moex_python_sdk.decorators import resp

from moex_python_sdk.models import new_resp_data
from moex_python_sdk.models.archives import (
    ArchiveYears, 
    ArchivePeriodParams,
    ArchivePeriod,
    ArchiveMonths,
)


class ArhiveApi:
    def __init__(self, api: BaseApi):
        self.api = api
        self.endpoint = "/archives"

    @resp
    def get_list_by_years(self, engine: str, market: str, datatype: str = "securities", format: str = "json"):
        """Список годов, за которые существуют ссылки на файлы с архивом сделок и исторической биржевой информацией. 
        * `datatype` может принимать значения securities или trades."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/{datatype}/years.{format}",
        )

        return r.url, ArchiveYears(years=new_resp_data(r["years"]))

    @resp
    def get_list_by_period(self, engine: str, market: str, datatype: str, period: str, params: ArchivePeriodParams, format: str = "json"):
        """Получить список ccылок на годовые/месячные/дневные файлы с архивом сделок и исторической биржевой информацией. 
        * `datatype` может принимать значения securities или trades. 
        * `period` может принимать значения yearly, monthly или daily. 
        Помесячные данные доступны только за последние 30 дней."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/{datatype}/{period}.{format}", 
            params=params.as_dict(),
        )

        return r.url, ArchivePeriod(files=new_resp_data(r["files"]))

    @resp
    def get_list_by_month(self, engine: str, market: str, datatype: str, year: str, format: str = "json"):
        """Список месяцев в году, за которые существуют ссылки на файлы с архивом сделок и исторической биржевой информацией. 
         * `datatype` может принимать значения securities или trades."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/{datatype}/years/{year}/months.{format}", 
        )
        
        return r.url, ArchiveMonths(months=new_resp_data(r["months"]))
    