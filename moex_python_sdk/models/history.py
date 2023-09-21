from typing import Optional
from pydantic import BaseModel

from moex_python_sdk.models import BaseParams, LangParams, RespData
from  moex_python_sdk.models.security_groups import SecurityGroupsCollectionSecurities


class HistoryBase(BaseModel):
    history: RespData

class History(BaseModel):
    history_dates: RespData


# listing
class HistoryListingParams(LangParams):
    start: Optional[int] = 0
    status: Optional[str] = "all" # Фильтр торгуемости инструментов: traded, nottraded или all

def new_history_listing_params(
        lang: str = "ru",
        start: int = 0,
        status: str = "all",
    ) -> HistoryListingParams:
    return HistoryListingParams(
        lang=lang,
        start=start,
        status=status,
    )


class HistorySession(BaseModel):
    trading_sessions: RespData


class HistorySecuritiesBaseParams(BaseParams):
    sort_order: Optional[str] = "asc" # Доступные значения 'asc' и 'desc'.
    sort_order_desc:Optional[str] # (Устарело)
    # Порядок сортировки.
    # Доступные значения Пусто и 'DESC'.
    numtrades: Optional[str] = "0" # Минимальное количество сделок с бумагой.
    start: Optional[int] = 0
    interim: Optional[str] = "0" # Показать промежуточные итоги торгов (только для валютного рынка)
    security_collection: Optional[str]
    assetcode: Optional[str]
    sort_column: Optional[str] = "secid" # Поле по которому сортируются выдача данных.
    limit: Optional[str] # Количество отдаваемых строк. Доступные значения: 100, 50, 20, 10, 5, 1
    tradingsession: Optional[str]
    # Показать данные только за необходимую сессию (только для фондового рынка)
    # 0 - Утренняя
    # 1 - Основная
    # 2 - Вечерняя
    # 3 - Итого
    security_type_id: Optional[str] # (! for history_cursor) Фильтровать по типу бумаг


class HistorySecuritiesParams(LangParams, HistorySecuritiesBaseParams):
    date: Optional[str] = "today"

def new_history_securities_params(
        lang: str = "ru",
        start: int = 0,
        sort_column: str = "secid",
        sort_order: str = "asc",
        sort_order_desc: str = None,
        date: str = "today",
        numtrades: str = "0",
        interim: str = "0",
        security_type_id: str = None,
        security_collection: str = None,
        assetcode: str = None,
        trading_session: str = None,
    ) -> HistorySecuritiesParams:
    return HistorySecuritiesParams(
        lang=lang,
        start=start,
        sort_column=sort_column,
        sort_order=sort_order,
        sort_order_desc=sort_order_desc,
        date=date,
        numtrades=numtrades,
        interim=interim,
        security_type_id=security_type_id,
        security_collection=security_collection,
        assetcode=assetcode,
        tradingsession=trading_session,
    )

class HistorySecurities(HistoryBase):
    history_cursor: RespData


class HistorySecurityParams(BaseParams):
    sort_order: Optional[str] = "asc"
    sort_order_desc:Optional[str]
    # Порядок сортировки.
    # Доступные значения Пусто и 'DESC'.
    from_at: Optional[str]
    till: Optional[str] = "2037-12-31"
    start: Optional[int] = 0
    numtrades: Optional[str] = "0" # Минимальное количество сделок с бумагой.
    limit: Optional[str] = "100"
    sort_column: Optional[str] = "TRADEDATE" # Поле по которому сортируются выдача данных.
    tradingsession: Optional[str]
    # Показать данные только за необходимую сессию (только для фондового рынка)
    # 0 - Утренняя
    # 1 - Основная
    # 2 - Вечерняя
    # 3 - Итого Фильтровать по типу бумаг

def new_history_security_params(
        lang: str = "ru",
        start: int = 0,
        sort_order: str = "asc",
        sort_order_desc: str = None,
        from_at: str = None,
        numtrades: str = "0",
        till: str = "2037-12-31" ,
        limit: str = "100",
        sort_column: str = "secid",
        tradingsession: str = None,
    ) -> HistorySecurityParams:
    return HistorySecurityParams(
        lang=lang,
        start=start,
        sort_order=sort_order,
        sort_order_desc=sort_order_desc,
        from_at=from_at,
        numtrades=numtrades,
        till=till,
        limit=limit,
        sort_column=sort_column,
        tradingsession=tradingsession,
    )


# history columns
class HistoryColumns(HistoryBase):
    history_yields: RespData


# history changeover
class HistoryChangeover(BaseModel):
    changeover: RespData


# zcyc
class HistoryZcycParams(BaseModel):
    date: Optional[str] = "today"
    time: Optional[str] # Если указано - выдается ближайшее значение КБД к данному моменту времени

    def as_dict(self):
        return self.model_dump(exclude_none=True)

def new_history_zcyc_params(date: str = "today", time: str = None,) -> HistoryZcycParams:
    return HistoryZcycParams(
        date=date,
        time=time,
    )

class HistoryZcyc(BaseModel):
    params: RespData


class HistoryYieldsParams(LangParams):
    sort_order: Optional[str] = "asc" # Доступные значения 'asc' и 'desc'.
    sort_order_desc:Optional[str]
    # Порядок сортировки.
    # Доступные значения Пусто и 'DESC'.
    date: Optional[str] = "today" # Фильтр торгуемости инструментов: traded, nottraded или all
    numtrades: Optional[str] = "0" # Минимальное количество сделок с бумагой.
    start: Optional[int] = 0
    interim: Optional[str] = "0" # Показать промежуточные итоги торгов (только для валютного рынка)
    security_collection: Optional[str]
    assetcode: Optional[str]
    sort_column: Optional[str] = "secid" # Поле по которому сортируются выдача данных.
    limit: Optional[str] # Количество отдаваемых строк. Доступные значения: 100, 50, 20, 10, 5, 1

def new_history_yields_params(
        lang: str = "ru",
        start: int = 0,
        sort_order: str = "asc",
        sort_order_desc: str = None,
        date: str = "today",
        numtrades: str = "0",
        interim: str = "0",
        security_collection: str = None,
        assetcode: str = None,
        sort_column: str = "secid",
        limit: str = None,
    ) -> HistoryYieldsParams:
    return HistoryYieldsParams(
        lang=lang,
        start=start,
        sort_order=sort_order,
        sort_order_desc=sort_order_desc,
        date=date,
        numtrades=numtrades,
        interim=interim,
        security_collection=security_collection,
        assetcode=assetcode,
        sort_column=sort_column,
        limit=limit,
    )

class HistoryYields(BaseModel):
    history_yields: RespData


# history dates
class HistoryDatesParams(LangParams):
    interim: Optional[str] = "0" # Показать промежуточные итоги торгов (только для валютного рынка)
    tradingsession: Optional[str]

def new_history_dates_params(
        interim: str = "0",
        tradingsession: str = None,
    ) -> HistoryDatesParams:
    return HistoryDatesParams(
        interim=interim,
        tradingsession=tradingsession,
    )

class HistoryDates(BaseModel):
    dates: RespData


class ActionBase(BaseModel):
    auctions: RespData
    auctions_dates: RespData


class HistoryBoardgroupsSecuritiesParams(HistorySecuritiesBaseParams):
    date: Optional[str] = "today"

def new_boardgroups_securities_params(
        interim: str = "0",
        tradingsession: str = None,
    ) -> HistoryDatesParams:
    return HistoryDatesParams(
        interim=interim,
        tradingsession=tradingsession,
    )

class HistoryBoardgroupsSecurities(HistorySecurities, ActionBase):
    ...


class HistoryBoardgroupsSecurity(HistorySecurities, ActionBase):
    auctions_cursor: RespData


# total
class HistoryTotalSecuritiesParams(LangParams):
    date: Optional[str] = "today"
    start: Optional[int] = 0
    tradingsession: Optional[str]

def new_history_total_securities_params(
        date: str = "0",
        start: int = 0,
        tradingsession: str = None,
    ) -> HistoryTotalSecuritiesParams:
    return HistoryTotalSecuritiesParams(
        date=date,
        start=start,
        tradingsession=tradingsession,
    )

class HistoryTotalSecurities(SecurityGroupsCollectionSecurities):
    securities_dates: RespData


class HistoryTotalSecurityParams(LangParams):
    from_at: Optional[str] = "1900-01-01"
    start: Optional[int] = 0
    till: Optional[str] = "2100-01-01"
    tradingsession: Optional[str]

def new_history_total_securities_params(
        from_at: str = "1900-01-01",
        start: int = 0,
        till: str = "2100-01-01",
        tradingsession: str = None,
    ) -> HistoryTotalSecurityParams:
    return HistoryTotalSecurityParams(
        from_at=from_at,
        start=start,
        till=till,
        tradingsession=tradingsession,
    )