from moex_python_sdk.api._api import BaseApi
from moex_python_sdk.decorators import resp

from moex_python_sdk.models import LangParams, new_resp_data
from moex_python_sdk.models.market import Markets
from moex_python_sdk.models.engines import (
    Engines,
    Engine,
    MarketOrderbook,
    Boards,
    Board,
    BoardsSecuritiesBase,
    BoardsSecuritiesParams,
    Securities,
    SecurityOrderbook,
    TradesBase,
    TradesParams,
    Trades,
    OrderbookParams,
    Orderbook,
    CandlesParams,
    Candles,
    BoardCandlebordersParams,
    BoardCandleborders,
    Boardgroups,
    Boardgroup,
    Candleborders,
    BoardgroupSecurity,
    BoardgroupOrderbook,
    Turnovers,
    SecstatsParams,
    Secstats,
    TurnoversParams,
    ZcycParams,
    Zcyc,
    Market,
    MarketZcycParams,
    MarketZcyc,
)


@resp
class EngineApi:
    def __init__(self, api: BaseApi):
        self.api = api
        self.endpoint = "/engines"

    def get_engines(self, params: LangParams, format: str = "json"):
        """Получить доступные торговые системы. Например: https://iss.moex.com/iss/engines.xml"""

        r = self.api.get(
            f"{self.endpoint}.{format}",
            params=params.as_dict(),
        )

        return r["url"], Engines(engines=new_resp_data(r["data"]["engines"]))

    def get_engine(self, engine: str, params: LangParams, format: str = "json"):
        """Получить описание и режим работы торговой системы. Например: https://iss.moex.com/iss/engines/stock.xml"""

        r = self.api.get(
            f"{self.endpoint}/{engine}.{format}",
            params=params.as_dict(),
        )

        return r["url"], Engine(
            engine=new_resp_data(r["data"]["engine"]),
            time_table=new_resp_data(r["data"]["timetable"]),
            daily_table=new_resp_data(r["data"]["dailytable"]),
        )

    def get_markets(self, engine: str, params: LangParams, format: str = "json"):
        """Получить список рынков торговой системы. Например: https://iss.moex.com/iss/engines/stock/markets.xml"""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets.{format}",
            params=params.as_dict(),
        )

        return r["url"], Markets(markets=new_resp_data(r["data"]["markets"]))

    def get_market(self, engine: str, market: str, params: LangParams, format: str = "json"):
        """Получить описание: словарь доступных режимов торгов, описание полей публикуемых таблиц данных и т.д. Например: https://iss.moex.com/iss/engines/stock/markets/shares.xml"""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}.{format}",
            params=params.as_dict(),
        )

        return r["url"], Market(
            boards=new_resp_data(r["data"]["boards"]),
            board_groups=new_resp_data(r["data"]["boardgroups"]),
            securities=new_resp_data(r["data"]["securities"]),
            market_data=new_resp_data(r["data"]["marketdata"]),
            trades=new_resp_data(r["data"]["trades"]),
            orderbook=new_resp_data(r["data"]["orderbook"]),
            history=new_resp_data(r["data"]["history"]),
            trades_hist=new_resp_data(r["data"]["trades_hist"]),
            market_data_yields=new_resp_data(r["data"]["marketdata_yields"]),
            trades_yields=new_resp_data(r["data"]["trades_yields"]),
            history_yields=new_resp_data(r["data"]["history_yields"]),
            secstats=new_resp_data(r["data"]["secstats"]),
        )

    def get_market_boards(self, engine: str, market: str, params: LangParams, format: str = "json"):
        """Получить справочник режимов торгов рынка. Например: https://iss.moex.com/iss/engines/stock/markets/shares/boards.xml"""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/boards.{format}",
            params=params.as_dict(),
        )

        return r["url"], Boards(
            boards=new_resp_data(r["data"]["boards"]),
        )

    def get_market_board(self, engine: str, market: str, board: str, params: LangParams, format: str = "json"):
        """Получить описание режима торгов. Например: https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR.xml"""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/boards/{board}.{format}",
            params=params.as_dict(),
        )

        return r["url"], Board(board=new_resp_data(r["data"]["board"]))

    def get_board_securities(self, engine: str, market: str, board: str, params: BoardsSecuritiesParams, format: str = "json"):
        """Получить таблицу инструментов по режиму торгов. Например: https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities.xml"""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/boards/{board}/securities.{format}",
            params=params.as_dict(),
        )

        return r["url"], Securities(
            securities=new_resp_data(r["data"]["securities"]),
            market_data=new_resp_data(r["data"]["marketdata"]),
            dataversion=new_resp_data(r["data"]["dataversion"]),
            market_data_yields=new_resp_data(r["data"]["marketdata_yields"]),
        )

    def get_board_security(self, engine: str, market: str, board: str, security: str, params: BoardsSecuritiesParams, format: str = "json"):
        """Получить данные по указанному инструменту на выбранном режиме торгов."""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/boards/{board}/securities/{security}.{format}",
            params=params.as_dict(),
        )

        return r["url"], Securities(
            securities=new_resp_data(r["data"]["securities"]),
            market_data=new_resp_data(r["data"]["marketdata"]),
            dataversion=new_resp_data(r["data"]["dataversion"]),
            market_data_yields=new_resp_data(r["data"]["marketdata_yields"]),
        )

    def get_board_trades(self, engine: str, market: str, board: str, security: str, params: TradesParams, format: str = "json"):
        """Получить все сделки указанного инструмента по выбранному режиму торгов."""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/boards/{board}/securities/{security}/trades.{format}",
            params=params.as_dict(),
        )

        return r["url"], Trades(
            trades=new_resp_data(r["data"]["trades"]),
            data_version=new_resp_data(r["data"]["dataversion"]),
            trades_yields=new_resp_data(r["data"]["trades_yields"]),
        )

    def get_board_security_orderbook(self, engine: str, market: str, board: str, security: str, params: OrderbookParams, format: str = "json"):
        """Получить стакан котировок указанного инструмента по выбранному режиму торгов."""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/boards/{board}/securities/{security}/orderbook.{format}",
            params=params.as_dict(),
        )

        return r["url"], SecurityOrderbook(
            orderbook=new_resp_data(r["data"]["orderbook"]),
            data_version=new_resp_data(r["data"]["dataversion"]),
        )

    def get_board_candles(self, engine: str, market: str, board: str, security: str, params: CandlesParams, format: str = "json"):
        """Получить свечи указанного инструмента по выбранному режиму торгов."""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/boards/{board}/securities/{security}/candles.{format}",
            params=params.as_dict(check=True),
        )

        return r["url"], Candles(candles=new_resp_data(r["data"]["candles"]))

    def get_board_candleborders(self, engine: str, market: str, board: str, security: str, params: BoardCandlebordersParams, format: str = "json"):
        """Получить период дат рассчитанных свечей."""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/boards/{board}/securities/{security}/candleborders.{format}",
            params=params.as_dict(),
        )

        return r["url"], BoardCandleborders(
            borders=new_resp_data(r["data"]["borders"]),
            durations=new_resp_data(r["data"]["durations"]),
        )

    def get_board_orderbook(self, engine: str, market: str, board: str, params: OrderbookParams, format: str = "json"):
        """Получить все лучшие котировки по выбранному режиму торгов."""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/boards/{board}/orderbook.{format}",
            params=params.as_dict(),

        )

        return r["url"], Orderbook(orderbook=new_resp_data(r["data"]["orderbook"]))

    def get_board_trades(self, engine: str, market: str, board: str, params: TradesParams, format: str = "json"):
        """Получить все сделки по выбранному режиму торгов."""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/boards/{board}/trades.{format}",
            params=params.as_dict(),
        )

        return r["url"], Trades(
            trades=new_resp_data(r["data"]["trades"]),
            data_version=new_resp_data(r["data"]["data_version"]),
            trades_yields=new_resp_data(r["data"]["trades_yields"]),
        )

    def get_market_boardgroups(self, engine: str, market: str, params: LangParams, format: str = "json"):
        """Получить справочник групп режимов торгов."""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/boardgroups.{format}",
            params=params.as_dict(),
        )

        return r["url"], Boardgroups(board_groups=new_resp_data(r["data"]["boardgroups"]))

    def get_market_boardgroup(self, engine: str, market: str, boardgroup: str, params: LangParams, format: str = "json"):
        """Получить описание группы режимов торгов."""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/boardgroups/{boardgroup}.{format}",
            params=params.as_dict(),
        )

        return r["url"], Boardgroup(board_group=new_resp_data(r["data"]["boardgroups"]))

    def get_boardgroup_candle(self, engine: str, market: str, boardgroup: str, security: str, params: CandlesParams, format: str = "json"):
        """Получить свечи указанного инструмента по выбранной группе режимов торгов."""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/boardgroups/{boardgroup}/securities/{security}/candle.{format}",
            params=params.as_dict(check=True)
        )
        print("r:", r)

        return r["url"], Candles(candles=new_resp_data(r["data"]["candles"]))

    def get_boardgroup_candleborders(self, engine: str, market: str, boardgroup: str, security: str, format: str = "json"):
        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/boardgroups/{boardgroup}/securities/{security}/candleborders.{format}",
        )

        return r["url"], Candleborders(borders=new_resp_data(r["data"]["borders"]))

    def get_boardgroup_securities(self, engine: str, market: str, boardgroup: str, params: BoardsSecuritiesParams, format: str = "json"):
        """Получить список всех инструментов, торгуемых на выбранной группе режимов торгов."""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/boardgroups/{boardgroup}/securities.{format}",
            params=params.as_dict(),
        )

        return r["url"], Securities(
            securities=new_resp_data(r["data"]["securities"]),
            market_data=new_resp_data(r["data"]["marketdata"]),
            data_version=new_resp_data(r["data"]["dataversion"]),
            market_data_yields=new_resp_data(r["data"]["marketdata_yields"]),
        )

    def get_boardgroup_security(self, engine: str, market: str, boardgroup: str, security: str, params: BoardsSecuritiesParams, format: str = "json"):
        """Получить данные по указанному инструменту, торгуемому на выбранной группе режимов торгов."""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/boardgroups/{boardgroup}/securities/{security}.{format}",
            params=params.as_dict(),
        )

        return r["url"], Securities(
            securities=new_resp_data(r["data"]["securities"]),
            market_data=new_resp_data(r["data"]["marketdata"]),
            data_version=new_resp_data(r["data"]["dataversion"]),
            market_data_yields=new_resp_data(r["data"]["marketdata_yields"]),
        )

    def get_boardgroup_orderbook_by_security(self, engine: str, market: str, boardgroup: str, security: str, params: OrderbookParams, format: str = "json"):
        """Получить лучшие заявки выбранного инструмента, торгуемого на выбранной группе режимов торгов."""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/boardgroups/{boardgroup}/securities/{security}/orderbook.{format}",
            params=params.as_dict(),
        )

        return r["url"], BoardgroupSecurity(
            orderbook=new_resp_data(r["data"]["orderbook"]),
            data_version=new_resp_data(r["data"]["dataversion"]),
        )

    def get_boardgroup_trades_by_security(self, engine: str, market: str, boardgroup: str, security: str, params: TradesParams, format: str = "json"):
        """Получить сделки выбранного инструмента, торгуемого на выбранной группе режимов торгов."""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/boardgroups/{boardgroup}/securities/{security}/trades.{format}",
            params=params.as_dict(),
        )

        return r["url"], Trades(
            trades=new_resp_data(r["data"]["trades"]),
            data_version=new_resp_data(r["data"]["dataversion"]),
            trades_yields=new_resp_data(r["data"]["trades_yields"]),
        )

    def get_boardgroup_orderbook(self, engine: str, market: str, boardgroup: str, params: OrderbookParams, format: str = "json"):
        """Получить лучшие заявки всех инструментов, торгуемых на выбранной группе режимов торгов."""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/boardgroups/{boardgroup}/orderbook.{format}",
            params=params.as_dict(),
        )

        return r["url"], BoardgroupOrderbook(
            trades=new_resp_data(r["data"]["trades"]),
            data_version=new_resp_data(r["data"]["dataversion"]),
        )

    def get_boardgroup_trades(self, engine: str, market: str, boardgroup: str, params: TradesParams, format: str = "json"):
        """Получить сделки инструментов, торгуемых на выбранной группе режимов торгов."""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/boardgroups/{boardgroup}/trades.{format}",
            params=params.as_dict(),
        )

        return r["url"], Trades(
            trades=new_resp_data(r["data"]["trades"]),
            data_version=new_resp_data(r["data"]["dataversion"]),
            trades_yields=new_resp_data(r["data"]["trades_yields"]),
        )

    def get_market_orderbook(self, engine: str, market: str, params: OrderbookParams, format: str = "json"):
        """Получить стаканы заявок всех инструментов рынка. Например: https://iss.moex.com/iss/engines/stock/markets/shares/orderbook.xml"""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/orderbook.{format}",
            params=params.as_dict()
        )

        return r["url"], MarketOrderbook(
            orderbook=new_resp_data(r["data"]["orderbook"]),
            data_version=new_resp_data(r["data"]["dataversion"]),
        )

    def get_orderbook_columns(self, engine: str, market: str, params: LangParams, format: str = "json"):
        """Получить описание полей для запросов стакана котировок для рынка. Например: https://iss.moex.com/iss/engines/stock/markets/shares/orderbook/columns.xml"""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/orderbook/columns.{format}",
            params=params.as_dict(),
        )

        return r["url"], Orderbook(orderbook=new_resp_data(r["data"]["orderbook"]))

    def get_market_trades(self, engine: str, market: str, params: TradesParams, format: str = "json"):
        """Получить все сделки рынка. Например: https://iss.moex.com/iss/engines/stock/markets/shares/trades.xml"""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/trades.{format}",
            params=params.as_dict(),
        )

        return r["url"], Trades(
            trades=new_resp_data(r["data"]["trades"]),
            data_version=new_resp_data(r["data"]["dataversion"]),
            trades_yields=new_resp_data(r["data"]["trades_yields"]),
        )

    def get_trades_columns(self, engine: str, market: str, params: LangParams, format: str = "json"):
        """Получить описание полей для запроса сделок по рынку. Например: https://iss.moex.com/iss/engines/stock/markets/shares/trades/columns.xml"""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/trades/columns.{format}",
            params=params.as_dict(),
        )

        return r["url"], TradesBase(trades=new_resp_data(r["data"]["trades"]))

    def get_market_turnovers(self, engine: str, market: str, params: LangParams, format: str = "json"):
        """Получить текущее значение оборота по рынку"""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/turnovers.{format}",
            params=params.as_dict(),
        )

        return r["url"], Turnovers(turnovers=new_resp_data(r["data"]["turnovers"]))

    def get_secstats(self, engine: str, market: str, params: SecstatsParams, format: str = "ru"):
        """Промежуточные "Итоги дня". Только для фондового рынка"""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/secstats.{format}",
            params=params.as_dict(),
        )

        return r["url"], Secstats(secstats=new_resp_data(r["data"]["secstats"]))

    def get_turnovers(self, engine: str, params: TurnoversParams, format: str = "json"):
        """Получить текущее значение оборотов торговой сессии по рынкам торговой системы"""

        r = self.api.get(
            f"{self.endpoint}/{engine}/turnovers.{format}",
            params=params.as_dict(),
        )

        return r["url"], Turnovers(turnovers=new_resp_data(r["data"]["turnovers"]))

    def get_zcyc(self, engine: str, params: ZcycParams, format: str = "ru"):
        """Получить все значения оборота по рынку"""

        r = self.api.get(
            f"{self.endpoint}/{engine}/zcyc.{format}",
            params=params.as_dict(),
        )

        return r["url"], Zcyc(
            turnovers=new_resp_data(r["data"]["turnovers"]),
            params=new_resp_data(r["data"]["params"]),
            params_dates=new_resp_data(r["data"]["params.dates"]),
            securities=new_resp_data(r["data"]["securities"]),
            securities_dates=new_resp_data(r["data"]["securities.dates"]),
            yearyields=new_resp_data(r["data"]["yearyields"]),
            yearyields_dates=new_resp_data(r["data"]["yearyields.dates"]),
        )

    def get_markets_zcyc(self, engine: str, params: MarketZcycParams, format: str = "ru"):
        """Получить данные по кривой бескупонной доходности (Прекращены расчеты с 2018-01-03)"""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/zcyc.{format}",
            params=params.as_dict(),
        )

        return r["url"], MarketZcyc(
            parameters=new_resp_data(r["data"]["parameters"]),
            values=new_resp_data(r["data"]["values"]),
        )

    def get_market_securities(self, engine: str, market: str, params: BoardsSecuritiesParams, format: str = "json"):
        """Получить таблицу инструментов торговой сессии по рынку в целом. Например: https://iss.moex.com/iss/engines/stock/markets/shares/securities.xml"""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/securities.{format}",
            params=params.as_dict(),
        )

        return r["url"], BoardsSecuritiesBase( securities=new_resp_data(r["data"]["securities"]))

    def get_securities_columns(self, engine: str, market: str, params: LangParams, format: str = "json"):
        """Получить описание полей для запросов публикуемых бумаг для рынка. Например: https://iss.moex.com/iss/engines/stock/markets/shares/securities/columns.xml"""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/securities/columns.{format}",
            params=params.as_dict(),
        )

        return r["url"], Securities(
            securities=new_resp_data(r["data"]["securities"]),
            market_data=new_resp_data(r["data"]["marketdata"]),
            data_version=new_resp_data(r["data"]["dataversion"]),
            market_data_yields=new_resp_data(r["data"]["marketdata_yields"]),
        )

    def get_market_security(self, engine: str, market: str, security: str, params: BoardsSecuritiesParams, format: str = "json"):
        """Получить данные по конкретному инструменту рынка. Например: https://iss.moex.com/iss/engines/stock/markets/shares/securities/AFLT.xml"""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/securities/{security}.{format}",
            params=params.as_dict(),
        )

        return r["url"], Securities(
            securities=new_resp_data(r["data"]["securities"]),
            market_data=new_resp_data(r["data"]["marketdata"]),
            data_version=new_resp_data(r["data"]["dataversion"]),
            market_data_yields=new_resp_data(r["data"]["marketdata_yields"]),
        )

    def get_security_orderbook(self, engine: str, market: str, security: str, params: OrderbookParams, format: str = "json"):
        """Получить стакан заявок по инструменту. Например: https://iss.moex.com/iss/engines/stock/markets/shares/securities/AFLT/orderbook.xml"""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/securities/{security}/orderbook.{format}",
            params=params.as_dict(),
        )

        return r["url"], SecurityOrderbook(
            orderbook=new_resp_data(r["data"]["orderbook"]),
            data_version=new_resp_data(r["data"]["dataversion"]),
        )

    def get_security_trades(self, engine: str, market: str, security: str, params: TradesParams, format: str = "json"):
        """Получить сделки по инструменту. Например: https://iss.moex.com/iss/engines/stock/markets/shares/securities/AFLT/trades.xml"""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/securities/{security}/trades.{format}",
            params=params.as_dict(),
        )

        return r["url"], TradesBase(trades=new_resp_data(r["data"]["trades"]))

    def get_security_candles(self, engine: str, market: str, security: str, params: CandlesParams, format: str = "json"):
        """Получить свечи указанного инструмента по дефолтной группе режимов."""

        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/securities/{security}/candles.{format}",
            params=params.as_dict(check=True),
        )

        return r["url"], TradesBase(candles=new_resp_data(r["data"]["candles"]))

    def get_security_candleborders(self, engine: str, market: str, security: str, format: str = "json"):
        r = self.api.get(
            f"{self.endpoint}/{engine}/markets/{market}/securities/{security}/candleborders.{format}",
        )

        return r["url"], Candleborders(borders=new_resp_data(r["data"]["borders"]))

