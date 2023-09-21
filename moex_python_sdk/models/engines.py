from typing import Optional
from pydantic import BaseModel

from moex_python_sdk.models import BaseParams, LangParams, RespData


class Engines(BaseModel):
    engines: RespData


class Engine(BaseModel):
    engine: RespData
    time_table: RespData
    daily_table: RespData


# candles
class CandlesParams(BaseParams):
    start: Optional[int] = 0
    till: Optional[str] = "2037-12-31"
    from_at: Optional[str]
    interval: Optional[str] = "10"
    iss_reverse: Optional[str] = "false"

def new_candles_params(
        start: Optional[int] = 0,
        till: Optional[str] = "2037-12-31" ,
        from_at: Optional[str] = None,
        interval: Optional[str] = "10",
        iss_reverse: Optional[str] = "false",
    ) -> CandlesParams:
    return CandlesParams(
        start=start,
        till=till,
        from_at=from_at,
        interval=interval,
        iss_reverse=iss_reverse,
    )

class Candles(BaseModel):
    candles: RespData # Свечи в формате HLOCV


# candleborders
class Candleborders(BaseModel):
    borders: RespData


# boards
class Boards(BaseModel):
    boards: RespData

class Market(Boards):
    board_groups: RespData
    securities: RespData
    market_data: RespData
    trades: RespData
    orderbook: RespData
    history: RespData
    trades_hist: RespData
    market_data_yields: RespData
    trades_yields: RespData
    history_yields: RespData
    secstats: RespData

class Board(BaseModel):
    board: RespData


# securities
class BoardsSecuritiesParams(LangParams):
    primary_board: Optional[str]
    assets: Optional[str]
    index: Optional[str]
    security_collection: Optional[str]
    previous_session: Optional[str] = "0"
    securities: Optional[str]
    first: Optional[str] = "0"
    sort_column: Optional[str]
    sort_order: Optional[str] = "asc"
    sectypes: Optional[str]
    leaders: Optional[str] = "0"
    nearest: Optional[str] = "0"
    seqnum: Optional[str] = "0"

def new_board_securities_params(
        lang: Optional[str] = "ru",
        primary_board: Optional[str] = None,
        assets: Optional[str] = None,
        index: Optional[str] = None,
        security_collection: Optional[str] = None,
        previous_session: Optional[str] = "0",
        securities: Optional[str] = None,
        first: Optional[str] = "0",
        sort_column: Optional[str] = None,
        sort_order: Optional[str] = "asc",
        sectypes: Optional[str] = None,
        leaders: Optional[str] = "0",
        nearest: Optional[str] = "0",
        seqnum: Optional[str] = "0",
    ) -> BoardsSecuritiesParams:
    return BoardsSecuritiesParams(
        lang=lang,
        primary_board=primary_board,
        assets=assets,
        index=index,
        security_collection=security_collection,
        previous_session=previous_session,
        securities=securities,
        first=first,
        sort_column=sort_column,
        sort_order=sort_order,
        sectypes=sectypes,
        leaders=leaders,
        nearest=nearest,
        seqnum=seqnum,
    )

class BoardsSecuritiesBase(BaseModel):
    securities: RespData

class Securities(BoardsSecuritiesBase):
    market_data: RespData
    data_version: RespData
    market_data_yields: RespData


# board trades
class TradesParams(BaseParams):
    tradeno: Optional[str]
    limit: Optional[str] = "5000"
    reversed: Optional[str] = "0"
    recno: Optional[str] = "0"
    previous_session: Optional[str] = "0"
    securities: Optional[str]
    next_trade: Optional[str] = "0"
    start: Optional[int] = 0
    yielddatetype: Optional[str]

def new_board_trades_params(
        tradeno: Optional[str] = None,
        limit: Optional[str] = "5000",
        reversed: Optional[str] = "0",
        recno: Optional[str] = "0",
        previous_session: Optional[str] = "0",
        securities: Optional[str] = None,
        next_trade: Optional[str] = "0",
        start: Optional[int] = 0,
        yielddatetype: Optional[str] = None,
    ) -> TradesParams:
    return TradesParams(
        tradeno=tradeno,
        limit=limit,
        reversed=reversed,
        recno=recno,
        previous_session=previous_session,
        securities=securities,
        next_trade=next_trade,
        start=start,
        yielddatetype=yielddatetype,
    )

class TradesBase(BaseModel):
    trades: RespData

class Trades(TradesBase):
    data_version: RespData
    trades_yields: RespData


# orderbook
class OrderbookParams(BaseParams):
    start: Optional[int] = 0
    seqnum: Optional[int] = None
    securities: Optional[str]

def new_orderbook_params(
        start: Optional[int] = 0,
        seqnum: Optional[int] = None,
        securities: Optional[str] = None,
    ) -> OrderbookParams:
    return OrderbookParams(
        start=start,
        seqnum=seqnum,
        securities=securities,
    )

class Orderbook(BaseModel):
    orderbook: RespData

class SecurityOrderbook(Orderbook):
    data_version: RespData


# board candleborders
class BoardCandlebordersParams(LangParams):
    ...

def new_board_candleborders_params(lang: str = "ru") -> BoardCandlebordersParams:
    return BoardCandlebordersParams(
        lang=lang,
    )

class BoardCandleborders(Candleborders):
    durations: RespData


# boardgroups
class Boardgroups(BaseModel):
    board_groups: RespData

class Boardgroup(BaseModel):
    board_group: RespData

class BoardgroupSecurity(BaseModel):
    orderbook: RespData
    data_version: RespData


class BoardgroupOrderbook(Orderbook):
    data_version: RespData

# markets
class Markets(BaseModel):
    markets: RespData

class MarketOrderbook(Orderbook):
    data_version: RespData


# turnovers
class TurnoversParams(LangParams):
    is_tonight_session: Optional[str] = "0"
    date: Optional[str] = "today"

def new_turnovers_params(
        lang: str = "ru",
        is_tonight_session: str = "0",
        date: str = "today",
        ) -> TurnoversParams:
    return TurnoversParams(
        lang=lang,
        is_tonight_session=is_tonight_session,
        date=date,
    )

class Turnovers(BaseModel):
    turnovers: RespData


# secstats
class SecstatsParams(BaseParams):
    tradingsession: Optional[str]
    # Показать данные только за необходимую сессию
    #  1 - Основная
    #  2 - Вечерняя
    #  3 - Итого
    securities: Optional[str]
    boardid: Optional[str]
    # Отфильтровать выдачу по режиму торгов.
    # Например: boardid=TQBR,SMAL (не более 10 режимов).

def new_secstats_params(
        tradingsession: str = None,
        securities: str = None,
        boardid: str = None,
        ) -> SecstatsParams:
    return SecstatsParams(
        tradingsession=tradingsession,
        securities=securities,
        boardid=boardid,
    )

class Secstats(BaseModel):
    secstats: RespData


# zcyc
class ZcycParams(LangParams):
    date: Optional[str] = "today"
    show: Optional[str]

def new_zcyc_params(
        lang: str = "ru",
        date: str = "today",
        show: str = None,
        ) -> ZcycParams:
    return ZcycParams(
        lang=lang,
        date=date,
        show=show,
    )

class Zcyc(BaseModel):
    maxdates: RespData
    params: RespData
    params_dates: RespData
    securities: RespData
    securities_dates: RespData
    yearyields: RespData
    yearyields_dates: RespData


# market zcyc
class MarketZcycParams(BaseParams):
    lang: Optional[str] = "ru"
    from_at: Optional[str] = "2000-01-01"
    start: Optional[int] = 0

def new_market_zcyc_params(
        lang: str = "ru",
        from_at: str = "2000-01-01",
        start: int = 0,
        ) -> MarketZcycParams:
    return MarketZcycParams(
        lang=lang,
        from_at=from_at,
        start=start,
    )

class MarketZcyc(BaseModel):
    parameters: RespData
    values: RespData

