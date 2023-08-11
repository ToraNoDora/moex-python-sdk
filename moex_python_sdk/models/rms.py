from typing import Optional, Dict
from pydantic import BaseModel

from moex_python_sdk.models import LangParams, RespData


# rms object
class RmsObjectParams(BaseModel):
    date: Optional[str] = "today" # !(only limits.dates)
    # Параметр работает, если не указан код инструмента.
    # С кодом инструмента используйте параметр &from= и &till=
    from_at: Optional[str] = "1970-01-01" # Для параметра должен быть указан код инструмента.
    till: Optional[str] = "1970-01-01" # Для параметра должен быть указан код инструмента.
    start: Optional[str] = "0"
    limit: Optional[str] = "1000"
    lang: Optional[str] # !(for limits)

    def as_dict(self):
        params = self.dict(exclude_none=True)
        params["from"] = params["from_at"]
        params.pop("from_at", None)

        return {k:v for k, v in params.items() if v is not None}

def new_rms_object_params(
        date: str = "today", 
        from_at: str = None, 
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
    staticparams: RespData
    staticparams_cursor: RespData
    staticparams_dates: RespData

class RmsObjectKeyterm(BaseModel):
    static_params_keyterm: RespData
    static_paramskeyterm_cursor: RespData
    static_paramskeyterm_dates: RespData

class RmsObjectPercentFutures(BaseModel):
    percent_futures: RespData
    percent_futures_cursor: RespData
    percent_futures_dates: RespData


# irr
class IrrParams(BaseModel):
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

    def as_dict(self):
        return self.dict(exclude_none=True)
    
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

