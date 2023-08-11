from moex_python_sdk.api._api import BaseApi
from moex_python_sdk.decorators import resp

from moex_python_sdk.models import new_resp_data
from moex_python_sdk.models.rms import (
    RmsObjectParams,
    RmsObject, 
    RmsObjectStat, 
    RmsObjectKeyterm, 
    RmsObjectPercentFutures,
    IrrParams, 
    Irr, 
    IrrFilters, 
    SettlementsCalendarParams,
    SettlementsCalendar,
)


class RmsApi:
    def __init__(self, api: BaseApi):
        self.api = api
        self.endpoint = "/rms"

    @resp
    def get_rms_object(self, engine: str, object: str, params: RmsObjectParams, format: str = "json"):
        """Минимальные ограничительные уровни ставок обеспечения и лимиты концентрации на срочном рынке."""

        r = self.api.get(
            f"{self.endpoint}/rms/engines/{engine}/objects/{object}.{format}", 
            params=params.as_dict(),
        )

        return r.url, RmsObject(
            limits=new_resp_data(r["limits"]),
            limits_cursor=new_resp_data(r["limits.cursor"]),
            limits_dates=new_resp_data(r["limits.dates"]),
        )

    @resp
    def get_rms_object_stat(self, engine: str, object: str, params: RmsObjectParams, format: str = "json"):
        """Статические параметры."""

        r = self.api.get(
            f"{self.endpoint}/rms/engines/{engine}/objects/{object}.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, RmsObjectStat(
            static_params=new_resp_data(r["staticparams"]),
            static_params_cursor=new_resp_data(r["staticparams.cursor"]),
            static_params_dates=new_resp_data(r["staticparams.dates"]),
        )

    @resp
    def get_rms_object_keyterm(self, engine: str, object: str, params: RmsObjectParams, format: str = "json"):
        """Статические параметры по ключевым срокам."""

        r = self.api.get(
            f"{self.endpoint}/rms/engines/{engine}/objects/{object}.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, RmsObjectKeyterm(
            limits=new_resp_data(r["limits"]),
            limits_cursor=new_resp_data(r["limits.cursor"]),
            limits_dates=new_resp_data(r["limits.dates"]),
        )  

    @resp
    def get_rms_object_percent_futures(self, engine: str, object: str, params: RmsObjectParams, format: str = "json"):
        """Параметры процентных фьючерсов."""

        r = self.api.get(
            f"{self.endpoint}/rms/engines/{engine}/objects/{object}.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, RmsObjectPercentFutures(
            percent_futures=new_resp_data(r["percentfutures"]),
            percent_futures_cursor=new_resp_data(r["percentfutures.cursor"]),
            percent_futures_dates=new_resp_data(r["percentfutures.dates"]),
        )

    @resp
    def get_irr(self, engine: str, params: IrrParams, format: str = "json"):
        """Индикаторы риска."""

        r = self.api.get(
            f"{self.endpoint}/rms/engines/{engine}/objects/irr.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, Irr(
            irr=new_resp_data(r["irr"]),
            irr_dates=new_resp_data(r["irr.dates"])
        )

    @resp
    def get_irr_filters(self, engine: str, format: str = "json"):
        """Доступные параметры фильтрации для индикаторов рисков."""

        r = self.api.get(
            f"{self.endpoint}/rms/engines/{engine}/objects/irr/filters.{format}", 
        )
        
        return r.url, IrrFilters(
            group_filters=new_resp_data(r["group.filters"]),
            currency_filters=new_resp_data(r["currency.filters"]),
            indicator_filters=new_resp_data(r["indicator.filters"]),
        )

    @resp
    def get_settlements_calendar(self, engine: str, params: SettlementsCalendarParams, format: str = "json"):
        """Календарь расчетных дней."""

        r = self.api.get(
            f"{self.endpoint}/rms/engines/{engine}/objects/settlementscalendar.{format}", 
            params=params.as_dict(),
        )

        return r.url, SettlementsCalendar(settlements_calendar=new_resp_data(r["settlements_calendar"]))
    

