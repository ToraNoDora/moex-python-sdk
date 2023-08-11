from moex_python_sdk.api import MoexApi
from moex_python_sdk.decorators import return_df


class History:
    def __init__(self, api: MoexApi):
        self.api = api.history()

    @return_df
    def get_board_by_dates(self, engine: str, market: str, board: str):
        return self.api.get_board_by_dates(engine, market, board)
    
    @return_df
    def get_board_listing(self, engine: str, market: str, board: str):
        return self.api.get_board_listing(engine, market, board)
    
    @return_df
    def get_board_securities(self, engine: str, market: str, board: str):
        return self.api.get_board_securities(engine, market, board)
    
    @return_df
    def get_board_security(self, engine: str, market: str, board: str, security: str):
        return self.api.get_board_security(engine, market, board, security)
    
    @return_df
    def get_board_security_dates(self, engine: str, market: str, board: str, security: str):
        return self.api.get_board_security_dates(engine, market, board, security)
    
    @return_df
    def get_board_yields(self, engine: str, market: str, board: str):
        return self.api.get_board_yields(engine, market, board)
    
    @return_df
    def get_board_yields_security(self, engine: str, market: str, board: str, security: str):
        return self.api.get_board_yields_security(engine, market, board, security)
    
    @return_df
    def get_boardgroup_dates(self, engine: str, market: str, boardgroup: str):
        return self.api.get_boardgroup_dates(engine, market, boardgroup)
    
    @return_df
    def get_boardgroup_listing_by_group(self, engine: str, market: str, boardgroup: str):
        return self.api.get_boardgroup_listing_by_group(engine, market, boardgroup)
    
    @return_df
    def get_boardgroup_securities(self, engine: str, market: str, boardgroup: str):
        return self.api.get_boardgroup_securities(engine, market, boardgroup)
    
    @return_df
    def get_boardgroup_security(self, engine: str, market: str, boardgroup: str, security: str):
        return self.api.get_boardgroup_security(engine, market, boardgroup, security)
    
    @return_df
    def get_boardgroup_security_by_dates(self, engine: str, market: str, boardgroup: str, security: str):
        return self.api.get_boardgroup_security_by_dates(engine, market, boardgroup, security)
    
    @return_df
    def get_boardgroup_listing_by_group(self, engine: str, market: str, boardgroup: str):
        return self.api.get_boardgroup_listing_by_group(engine, market, boardgroup)
    
    @return_df
    def get_boardgroup_yields(self, engine: str, market: str, boardgroup: str):
        return self.api.get_boardgroup_yields(engine, market, boardgroup)
    
    @return_df
    def get_boardgroup_yields(self, engine: str, market: str, boardgroup: str, security: str):
        return self.api.get_boardgroup_yields(engine, market, boardgroup, security)
    
    @return_df
    def get_market_dates(self, engine: str, market: str):
        return self.api.get_market_dates(engine, market)
    
    @return_df
    def get_listing(self, engine: str, market: str):
        return self.api.get_listing(engine, market)
    
    @return_df
    def get_listing_columns(self, engine: str, market: str):
        return self.api.get_listing_columns(engine, market)
    
    @return_df
    def get_securities_columns(self, engine: str, market: str):
        return self.api.get_securities_columns(engine, market)
    
    # TODO args
    @return_df
    def get_market_securities(self, engine: str, market: str):
        return self.api.get_market_securities(engine, market)
    
    @return_df
    def get_security(self, engine: str, market: str, security: str):
        return self.api.get_security(engine, market, security)
    
    @return_df
    def get_security_by_dates(self, engine: str, market: str, security: str):
        return self.api.get_security_by_dates(engine, market, security)
    
    @return_df
    def get_market_sessions(self, engine: str, market: str):
        return self.api.get_market_sessions(engine, market)
    
    @return_df
    def get_board_by_securities(self, engine: str, market: str, session: str, board: str):
        return self.api.get_board_by_securities(engine, market, session, board)
    
    @return_df
    def get_board_by_security(self, engine: str, market: str, session: str, board: str, security: str):
        return self.api.get_board_by_security(engine, market, session, board, security)
    
    @return_df
    def get_boardgroup_by_securities(self, engine: str, market: str, session: str, boardgroup: str):
        return self.api.get_boardgroup_by_securities(engine, market, session, boardgroup)
    
    @return_df
    def get_boardgroup_by_security(self, engine: str, market: str, session: str, boardgroup: str, security: str):
        return self.api.get_boardgroup_by_security(engine, market, session, boardgroup, security)
    
    # TODO args
    @return_df
    def get_session_by_securities(self, engine: str, market: str, session: str):
        return self.api.get_session_by_securities(engine, market, session)
    
    @return_df
    def get_session_by_security(self, engine: str, market: str, session: str, security: str):
        return self.api.get_session_by_security(engine, market, session, security)
    
    @return_df
    def get_market_yields(self, engine: str, market: str):
        return self.api.get_market_yields(engine, market)
    
    @return_df
    def get_market_yield(self, engine: str, market: str, security: str):
        return self.api.get_market_yield(engine, market, security)
    
    @return_df
    def get_securities_changeover(self):
        return self.api.get_securities_changeover()
    
    @return_df
    def get_stock_totals_boards(self):
        return self.api.get_stock_totals_boards()
    
    @return_df
    def get_stock_totals_board_by_securities(self, board: str):
        return self.api.get_stock_totals_board_by_securities(board)
    
    @return_df
    def get_stock_totals_board_by_security(self, board: str, security: str):
        return self.api.get_stock_totals_board_by_security(board, security)
    
    @return_df
    def get_stock_totals_securities(self):
        return self.api.get_stock_totals_securities()
    
    @return_df
    def get_stock_zcyc(self):
        return self.api.get_stock_zcyc()

    @return_df
    def get_markets_info(self):
        return self.api.get_markets_info()
    
    @return_df
    def get_daily_market_info(self, market: str):
        return self.api.get_daily_market_info(market)
    
    @return_df
    def get_monthly_market_info(self, market: str):
        return self.api.get_monthly_market_info(market)
    
