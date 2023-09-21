from typing import Optional
from pydantic import BaseModel

from moex_python_sdk.models import BaseParams, LangParams, RespData


# object
class RmsObjects(BaseModel):
    objects: RespData

class RmsObjectParams(BaseParams):
    date: Optional[str] = "today"
    # Параметр работает, если не указан код инструмента.
    # С кодом инструмента используйте параметр &from= и &till=
    from_at: Optional[str] = "1970-01-01" # Для параметра должен быть указан код инструмента.
    till: Optional[str] = "1970-01-01" # Для параметра должен быть указан код инструмента.
    start: Optional[str] = "0"
    limit: Optional[str] = "1000"
    lang: Optional[str]

def new_rms_object_params(
        date: str = "today",
        from_at: str = "1970-01-01",
        till: str = None,
        start: str = "0",
        limit: str = "1000",
        lang: str = None,
    ) -> RmsObjectParams:
    return RmsObjectParams(
        date=date,
        from_at=from_at,
        till=till,
        start=start,
        limit=limit,
        lang=lang,
    )

class RmsObject(BaseModel):
    limits: RespData
    limits_cursor: RespData
    limits_dates: RespData

class RmsObjectStat(BaseModel):
    static_params: RespData
    static_params_cursor: RespData

class RmsObjectMarketRates(BaseModel):
    market_rates: RespData
    market_rates_dates: RespData
    market_rates_cursor: RespData

class RmsObjectPercentFutures(BaseModel):
    percent_futures: RespData
    percent_futures_cursor: RespData
    percent_futures_dates: RespData


# irr
class IrrParams(BaseParams):
    date: str = "today"
    q: str # Поиск по инструментам
    group: Optional[str]
    # Фильтр по полю "Множество" ("group").
    # Можно использовать можно через запятую указывать несколько значений (не более 5 элементов).
    # Поиск по подстроке невозможен.
    indicator: Optional[str]
    # Фильтр по полю "Индикатор множества" ("indicator").
    # Можно использовать можно через запятую указывать несколько значений (не более 5 элементов).
    # Поиск по подстроке невозможен.
    currencyid: Optional[str]
    # Фильтр по полю "Валюта риска" ("currencyid)".
    # Можно использовать можно через запятую указывать несколько значений (не более 5 элементов). Поиск по подстроке невозможен.
    instrument: Optional[str]
    # Фильтр по полю "Торговый код бумаги" ("instrument)".
    # Можно использовать можно через запятую указывать несколько значений (не более 5 элементов). Поиск по подстроке невозможен.
    isin: Optional[str]
    # Фильтр по полю "ISIN" ("ISIN)".
    # Можно использовать можно через запятую указывать несколько значений (не более 5 элементов). Поиск по подстроке невозможен.

def new_irr_params(
        date: str = "today",
        q: str = None,
        group: str = None,
        indicator: str = None, currencyid: str = None,
        instrument: str = None,
        isin: str = None,
    ) -> IrrParams:
    return IrrParams(
        date=date,
        q=q,
        group=group,
        indicator=indicator,
        currencyid=currencyid,
        instrument=instrument,
        isin=isin,
    )

class Irr(BaseModel):
    irr: RespData
    irr_dates: RespData


class IrrFilters(BaseModel):
    group_filters: RespData
    indicator_filters: RespData
    currency_filters: RespData


# settlements_calendar
class SettlementsCalendarParams(LangParams):
    year: Optional[str]  = "today"

def new_settlements_calendar_params(year: str = "today", lang: str = "ru") -> SettlementsCalendarParams:
    return SettlementsCalendarParams(
        year=year,
        lang=lang,
    )

class SettlementsCalendar(BaseModel):
    settlements_calendar: RespData

