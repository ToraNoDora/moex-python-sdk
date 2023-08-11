from moex_python_sdk.api._api import BaseApi
from moex_python_sdk.decorators import resp

from moex_python_sdk.models import new_resp_data
from moex_python_sdk.models import LangParams, DateParams, MonthParams
from moex_python_sdk.models.boards import Boards
from moex_python_sdk.models.market import Markets
from moex_python_sdk.models.history import (
    HistoryBase,
    History,
    HistoryListingParams,
    HistorySession,
    HistorySecuritiesParams,
    HistorySecurities,
    HistorySecurityParams,
    HistoryColumns,
    HistoryChangeover,
    HistoryZcycParams,
    HistoryZcyc,
    HistoryYieldsParams,
    HistoryYields,
    HistoryDatesParams,
    HistoryDates,
    HistoryBoardgroupsSecuritiesParams,
    HistoryBoardgroupsSecurities,
    HistoryBoardgroupsSecurity,
    HistoryTotalSecuritiesParams,
    HistoryTotalSecurities,
    HistoryTotalSecurityParams,
)
from moex_python_sdk.models.securities import Securities


class HistoryApi:
    def __init__(self, api: BaseApi):
        self.api = api
        self.endpoint = "/history"


    @resp
    def get_board_by_dates(self, engine: str, market: str, board: str, params: HistoryDatesParams, format: str = "json"):
        """Получить интервал дат, доступных в истории для рынка по заданному режиму торгов."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/boards/{board}/dates.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistoryDates(dates=new_resp_data(r["dates"]))
    
    @resp
    def get_board_listing(self, engine: str, market: str, board: str, params: HistoryListingParams, format: str = "json"):
        """Получить данные по листингу бумаг в историческом разрезе по указанному режиму."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/boards/{board}/listing.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, Securities(securities=new_resp_data(r["securities"]))
    
    @resp
    def get_board_securities(self, engine: str, market: str, board: str, params: HistorySecuritiesParams, format: str = "json"):
        """Получить историю торгов для всех бумаг на указанном режиме торгов отфильтрованных по дате."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/boards/{board}/securities.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistorySecurities(
            history=new_resp_data(r["history"]),
            history_cursor=new_resp_data(r["history.cursor"]),
        )
        
    
    @resp
    def get_board_security(self, engine: str, market: str, board: str, security: str, params: HistorySecurityParams, format: str = "json"):
        """Получить историю торгов для указанной бумаги на указанном режиме торгов за указанный интервал дат."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/boards/{board}/securities/{security}.{format}",
            params=params.as_dict(),
        )
        
        return r.url, HistoryBase(history=new_resp_data(r["history"]))
    
    @resp
    def get_board_security_dates(self, engine: str, market: str, board: str, security: str, params: HistoryDatesParams, format: str = "json"):
        """Получить интервал дат в истории, за которые доступна указанная бумага на рынке на указанном режиме торгов."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/boards/{board}/securities/{security}/dates.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistoryDates(dates=new_resp_data(r["dates"]))
    
    @resp
    def get_board_yields(self, engine: str, market: str, board: str, params: HistoryYieldsParams, format: str = "json"):
        """Получить историю доходностей для всех бумаг на указанном режиме торгов отфильтрованных по дате."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/boards/{board}/yields.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistoryYields(history_yield=new_resp_data(r["history.yields"])) 
    
    @resp
    def get_board_yields_security(self, engine: str, market: str, board: str, security: str, params: HistorySecurityParams, format: str = "json"):
        """Получить историю доходностей для указанной бумаги на указанном режиме торгов за указанный интервал дат."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/boards/{board}/yields/{security}.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistoryYields(history_yield=new_resp_data(r["history.yields"]))  
    
    @resp
    def get_boardgroup_dates(self, engine: str, market: str, boardgroup: str, params: HistoryDatesParams, format: str = "json"):
        """Получить интервал дат для указанной группы режимов торгов."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/boardgroups/{boardgroup}/dates.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistoryDates(dates=new_resp_data(r["dates"]))  
    
    @resp
    def get_boardgroup_listing_by_group(self, engine: str, market: str, boardgroup: str, params: HistoryListingParams, format: str = "json"):
        """Получить данные по листингу бумаг в историческом разрезе по указанной группе режимов."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/boardgroups/{boardgroup}/listing.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, Securities(securities=new_resp_data(r["securities"]))
    
    @resp
    def get_boardgroup_securities(self, engine: str, market: str, boardgroup: str, params: HistoryBoardgroupsSecuritiesParams, format: str = "json"):
        """Получить историю аукционов даркпул отфильтрованных по дате."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/boardgroups/{boardgroup}/securities.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistorySecurities(
            history=new_resp_data(r["history"]),
            history_cursor=new_resp_data(r["history.cursor"]),
        )
    
    @resp
    def get_boardgroup_securities_with_action(self, engine: str, market: str, boardgroup: str, params: HistoryBoardgroupsSecuritiesParams, format: str = "json"):
        """Получить историю аукционов даркпул отфильтрованных по дате."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/boardgroups/{boardgroup}/securities.{format}",
            params=params.as_dict(),
        )
        
        return r.url, HistoryBoardgroupsSecurities(
            history=new_resp_data(r["history"]),
            history_cursor=new_resp_data(r["history.cursor"]),
            auctions=new_resp_data(r["auctions"]),
            auctions_dates=new_resp_data(r["auctions.dates"]),
        )
    
    @resp
    def get_boardgroup_security(self, engine: str, market: str, boardgroup: str, security: str, params: HistorySecurityParams, format: str = "json"):
        """Получить интервал дат для указанной бумаги на заданной группе режимов торгов."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/boardgroups/{boardgroup}/securities/{security}/dates.{format}",
            params=params.as_dict(),
        )
        
        return r.url, HistoryBoardgroupsSecurity(
            history=new_resp_data(r["history"]),
            auctions=new_resp_data(r["auctions"]),
            auctions_dates=new_resp_data(r["auctions.dates"]),
            history_cursor=new_resp_data(r["history.cursor"]),
        )
    
    @resp
    def get_boardgroup_security_with_interval(self, engine: str, market: str, boardgroup: str, security: str, params: HistorySecurityParams, format: str = "json"):
        """Получить интервал дат для указанной бумаги на заданной группе режимов торговза указанный интервал дат."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/boardgroups/{boardgroup}/securities/{security}.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistorySecurities(
            history=new_resp_data(r["history"]),
            history_cursor=new_resp_data(r["history.cursor"]),
        )

    @resp
    def get_boardgroup_security_by_dates(self, engine: str, market: str, boardgroup: str, security: str, params: HistoryDatesParams, format: str = "json"):
        """Получить интервал дат для указанной бумаги на заданной группе режимов торгов."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/boardgroups/{boardgroup}/securities/{security}/dates.{format}", 
            params=params.as_dict(),
        )

        return r.url, HistoryDates(dates=new_resp_data(r["dates"]))
    
    @resp
    def get_boardgroup_yields(self, engine: str, market: str, boardgroup: str, params: HistoryYieldsParams, format: str = "json"):
        """Получить доходности торгов для всех бумаг на указанной группе режимов торгов за указанную дату."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/boardgroups/{boardgroup}/yields.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistoryYields(history_yields=new_resp_data(r["history_yields"]))
    
    @resp
    def get_boardgroup_yields(self, engine: str, market: str, boardgroup: str, security: str, params: HistorySecuritiesParams, format: str = "json"):
        """Получить историю доходностей для указанной бумаги на выбранной группе режимов торгов за указанный интервал дат."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/boardgroups/{boardgroup}/yields/{security}.{format}", 
            params=params.as_dict(),
        )

        return r.url, HistoryYields(history_yields=new_resp_data(r["history_yields"]))
    
    @resp
    def get_market_dates(self, engine: str, market: str, params: HistoryDatesParams, format: str = "json"):
        """Получить даты, за которые доступны данные на указанных рынке и торговой системе."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/dates.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistoryDates(dates=new_resp_data(r["dates"]))
    
    @resp
    def get_listing(self, engine: str, market: str, params: HistoryListingParams, format: str = "json"):
        """Список неторгуемых инструментов с указанием интервалов торгуемости по режимам."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/listing.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, Securities(securities=new_resp_data(r["securities"]))
    
    @resp
    def get_listing_columns(self, engine: str, market: str, params: LangParams, format: str = "json"):
        """Получить описание полей для запросов торгуемости бумаг (листинга)."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/listing/columns.{format}", 
            params=params.as_dict(),
        )

        return r.url, Securities(securities=new_resp_data(r["securities"]))
    
    @resp
    def get_securities_columns(self, engine: str, market: str, params: LangParams, format: str = "json"):
        """Получить описание полей для запросов исторических данных по бумагам для рынка."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/securities/columns.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistoryColumns(
            history=new_resp_data(r["history_yields"]),
            history_yields=new_resp_data(r["history_yields"]),
        )
    
    @resp
    def get_market_securities(self, engine: str, market: str, params: HistorySecuritiesParams, format: str = "json"):
        """Получить историю по всем бумагам на рынке за одну дату. Например: https://iss.moex.com/iss/history/engines/stock/markets/index/securities.xml?date=2010-11-22"""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/securities.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistorySecurities(
            history=new_resp_data(r["history"]),
            history_cursor=new_resp_data(r["history.cursor"]),
        )
    
    @resp
    def get_security(self, engine: str, market: str, security: str, params: HistorySecurityParams, format: str = "json"):
        """Получить историю по одной бумаге на рынке за интервал дат."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/securities/{security}.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistorySecurities(
            history=new_resp_data(r["history"]),
            history_cursor=new_resp_data(r["history.cursor"]),
        )
    
    @resp
    def get_security_by_dates(self, engine: str, market: str, security: str, params: HistoryDatesParams, format: str = "json"):
        """Получить интервал дат в истории для указанного рынка и бумаги."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/securities/{security}/dates.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistoryDates(dates=new_resp_data(r["dates"]))
    
    @resp
    def get_market_sessions(self, engine: str, market: str, params: LangParams, format: str = "json"):
        """Список сессий доступных в итогах торгов. Только для фондового рынка!"""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/sessions.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistorySession(trading_sessions=new_resp_data(r["trading_sessions"]))
    
    @resp
    def get_board_by_securities(self, engine: str, market: str, session: str, board: str, params: HistorySecuritiesParams, format: str = "json"):
        """Получить историю торгов для всех бумаг на указанном режиме торгов отфильтрованных по дате."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/sessions/{session}/boards/{board}/securities.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistorySecurities(
            history=new_resp_data(r["history"]),
            history_cursor=new_resp_data(r["history.cursor"]),
        )

    @resp
    def get_board_by_security(self, engine: str, market: str, session: str, board: str, security: str, params: HistorySecurityParams, format: str = "json"):
        """Получить историю торгов для указанной бумаги на указанном режиме торгов за указанный интервал дат."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/sessions/{session}/boards/{board}/securities/{security}.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistorySecurities(
            history=new_resp_data(r["history"]),
            history_cursor=new_resp_data(r["history.cursor"]),
        )
    
    @resp
    def get_boardgroup_by_securities(self, engine: str, market: str, session: str, boardgroup: str, params: HistorySecuritiesParams, format: str = "json"):
        """Получить историю торгов для всех бумаг на указанной группе режимов торгов за указанную дату."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/sessions/{session}/boardgroups/{boardgroup}/securities.{format}", 
            params=params.as_dict(),
        )

        return r.url, HistorySecurities(
            history=new_resp_data(r["history"]),
            history_cursor=new_resp_data(r["history.cursor"]),
        )

    @resp
    def get_boardgroup_by_security(self, engine: str, market: str, session: str, boardgroup: str, security: str, params: HistorySecurityParams, format: str = "json"):
        """Получить историю торгов для указанной бумаги на выбранной группе режимов торгов за указанный интервал дат."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/sessions/{session}/boardgroups/{boardgroup}/securities/{security}.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistorySecurities(
            history=new_resp_data(r["history"]),
            history_cursor=new_resp_data(r["history.cursor"]),
        )
    
    @resp
    def get_session_by_securities(self, engine: str, market: str, session: str, params: HistorySecuritiesParams, format: str = "json"):
        """Получить историю по всем бумагам на рынке за одну дату. Например: https://iss.moex.com/iss/history/engines/stock/markets/index/securities.xml?date=2010-11-22"""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/sessions/{session}/securities.{format}", 
            params=params.as_dict(),
        )
    
        return r.url, HistorySecurities(
            history=new_resp_data(r["history"]),
            history_cursor=new_resp_data(r["history.cursor"]),
        )
    
    @resp
    def get_session_by_security(self, engine: str, market: str, session: str, security: str, params: HistorySecurityParams, format: str = "json"):
        """Получить историю по одной бумаге на рынке за интервал дат."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/sessions/{session}/securities/{security}.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistorySecurities(
            history=new_resp_data(r["history"]),
            history_cursor=new_resp_data(r["history.cursor"]),
        )

    @resp
    def get_market_yields(self, engine: str, market: str, params: HistoryYieldsParams, format: str = "json"):
        """Получить историю рассчитанных доходностей для всех бумаг на указанном режиме торгов отфильтрованных по дате."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/yields.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistoryYields(history_yields=new_resp_data(r["history_yields"]))
    
    @resp
    def get_market_yield(self, engine: str, market: str, params: HistorySecurityParams, security: str, format: str = "json"):
        """Получить историю доходностей по одной бумаге на рынке за интервал дат."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/yields/{security}.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistoryYields(history_yields=new_resp_data(r["history_yields"]))
    
    @resp
    def get_securities_changeover(self, format: str = "json"):
        """Информация по техническому изменению торговых кодов."""

        r = self.api.get(
            f"{self.endpoint}/engines/stock/markets/shares/securities/changeover.{format}", 
        )
        
        return r.url, HistoryChangeover(changeover=new_resp_data(r["changeover"]))
    
    @resp
    def get_stock_totals_boards(self, format: str = "json"):
        """Список режимов обобщенной информации по фондовому рынку."""

        r = self.api.get(
            f"{self.endpoint}/engines/stock/totals/boards.{format}", 
        )
        
        return r.url, Boards(boards=new_resp_data(r["boards"]))
    
    @resp
    def get_stock_totals_board_by_securities(self, board: str, params: HistoryTotalSecuritiesParams, format: str = "json"):
        """Обобщенная информация по фондовому рынку по выбранному режиму."""

        r = self.api.get(
            f"{self.endpoint}/engines/stock/totals/boards/{board}/securities.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistoryTotalSecurities(
            securities=new_resp_data(r["securities"]),
            securities_cursor=new_resp_data(r["securities.cursor"]),
            securities_dates=new_resp_data(r["securities.dates"]),
        )
    

    @resp
    def get_stock_totals_board_by_security(self, board: str, security: str, params: HistoryTotalSecurityParams, format: str = "json"):
        """Обобщенная информация по фондовому рынку по выбранному режиму и инструменту."""

        r = self.api.get(
            f"{self.endpoint}/engines/stock/totals/boards/{board}/securities/{security}.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistoryTotalSecurities(
            securities=new_resp_data(r["securities"]),
            securities_cursor=new_resp_data(r["securities.cursor"]),
            securities_dates=new_resp_data(r["securities.dates"]),
        )
    
    @resp
    def get_stock_totals_securities(self, params: HistoryTotalSecuritiesParams, format: str = "json"):
        """Обобщенная информация по фондовому рынку."""

        r = self.api.get(
            f"{self.endpoint}/engines/stock/totals/securities.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistoryTotalSecurities(
            securities=new_resp_data(r["securities"]),
            securities_cursor=new_resp_data(r["securities.cursor"]),
            securities_dates=new_resp_data(r["securities.dates"]),
        )
    
    @resp
    def get_stock_zcyc(self, params: HistoryZcycParams, format: str = "json"):
        """История изменения параметров КБД (Кривая Бескупоной Доходности)."""

        r = self.api.get(
            f"{self.endpoint}/engines/stock/zcyc.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, HistoryZcyc(params=new_resp_data(r["params"]))
    
    @resp
    def get_markets_info(self, params: LangParams, format: str = "ru"):
        """Обобщенные данные ОТС ПФИ и РЕПО - список рынков."""

        r = self.api.get(
            f"{self.endpoint}/otc/providers/nsd/markets.{format}", 
            params=params.as_dict(),
        )

        return r.url, Markets(markets=new_resp_data(r["markets"]))
    
    @resp
    def get_daily_market_info(self, market: str, params: DateParams, format: str = "ru"):
        """Ежедневные обобщенные данные ОТС ПФИ и РЕПО."""

        r = self.api.get(
            f"{self.endpoint}/otc/providers/nsd/markets/{market}/daily.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, History(
            history=new_resp_data(r["history"]),
            history_dates=new_resp_data(r["history.dates"]),
        )
    
    @resp
    def get_monthly_market_info(self, market: str, params: MonthParams, format: str = "ru"):
        """Ежемесячные обобщенные данные ОТС ПФИ и РЕПО."""

        r = self.api.get(
            f"{self.endpoint}/otc/providers/nsd/markets/{market}/monthly.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, History(
            history=new_resp_data(r["history"]),
            history_dates=new_resp_data(r["history.dates"]),
        )
    