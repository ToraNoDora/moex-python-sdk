from moex_python_sdk.api._api import BaseApi
from moex_python_sdk.decorators import resp

from moex_python_sdk.models import new_resp_data
from moex_python_sdk.models.rms import (
    RmsObjects,
    RmsObjectParams,
    RmsObject,
    RmsObjectStat,
    RmsObjectMarketRates,
    RmsObjectPercentFutures,
    IrrParams,
    Irr,
    IrrFilters,
    SettlementsCalendarParams,
    SettlementsCalendar,
)


@resp
class RmsApi:
    def __init__(self, api: BaseApi):
        self.api = api
        self.endpoint = "/rms"

    def get_rms_objects(self, engine: str, format: str = "json"):
        """Минимальные ограничительные уровни ставок обеспечения и лимиты концентрации на срочном рынке."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/objects.{format}",
        )

        return r["url"], RmsObjects(objects=new_resp_data(r["data"]["objects"]))

    def get_rms_object_limits(self, engine: str, params: RmsObjectParams, format: str = "json"):
        """Минимальные ограничительные уровни ставок обеспечения и лимиты концентрации на срочном рынке."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/objects/limits.{format}",
            params=params.as_dict(check=True),
        )

        return r["url"], RmsObject(
            limits=new_resp_data(r["data"]["limits"]),
            limits_cursor=new_resp_data(r["data"]["limits.cursor"]),
            limits_dates=new_resp_data(r["data"]["limits.dates"]),
        )

    def get_rms_object_stat(self, engine: str, params: RmsObjectParams, format: str = "json"):
        """Статические параметры."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/objects/staticparams.{format}",
            params=params.as_dict(check=True),
        )

        return r["url"], RmsObjectStat(
            static_params=new_resp_data(r["data"]["staticparams"]),
            static_params_cursor=new_resp_data(r["data"]["staticparams.cursor"]),
        )

    def get_rms_object_market_rates(self, engine: str, params: RmsObjectParams, format: str = "json"):
        """Статические параметры по рыночным рискам."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/objects/marketrates.{format}",
            params=params.as_dict(check=True),
        )

        return r["url"], RmsObjectMarketRates(
            market_rates=new_resp_data(r["data"]["marketrates"]),
            market_rates_cursor=new_resp_data(r["data"]["marketrates.cursor"]),
            market_rates_dates=new_resp_data(r["data"]["marketrates.dates"]),
        )

    def get_rms_object_percent_futures(self, engine: str, params: RmsObjectParams, format: str = "json"):
        """Параметры процентных фьючерсов."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/objects/percentfutures.{format}",
            params=params.as_dict(),
        )

        return r["url"], RmsObjectPercentFutures(
            percent_futures=new_resp_data(r["data"]["percentfutures"]),
            percent_futures_cursor=new_resp_data(r["data"]["percentfutures.cursor"]),
            percent_futures_dates=new_resp_data(r["data"]["percentfutures.dates"]),
        )

    def get_object_irr(self, engine: str, params: IrrParams, format: str = "json"):
        """Индикаторы риска."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/objects/irr.{format}",
            params=params.as_dict(),
        )

        return r["url"], Irr(
            irr=new_resp_data(r["data"]["irr"]),
            irr_dates=new_resp_data(r["data"]["irr.dates"])
        )

    def get_object_irr_filters(self, engine: str, format: str = "json"):
        """Доступные параметры фильтрации для индикаторов рисков."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/objects/irr/filters.{format}",
        )

        return r["url"], IrrFilters(
            group_filters=new_resp_data(r["data"]["group.filters"]),
            currency_filters=new_resp_data(r["data"]["currency.filters"]),
            indicator_filters=new_resp_data(r["data"]["indicator.filters"]),
        )

    def get_object_settlements_calendar(self, engine: str, params: SettlementsCalendarParams, format: str = "json"):
        """Календарь расчетных дней."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/objects/settlementscalendar.{format}",
            params=params.as_dict(),
        )

        return r["url"], SettlementsCalendar(settlements_calendar=new_resp_data(r["data"]["settlements_calendar"]))

