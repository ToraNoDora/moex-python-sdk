from moex_python_sdk.api import MoexApi
from moex_python_sdk.decorators import return_df


class Engine:
    def __init__(self, api: MoexApi):
        self.api = api.engine()

    @return_df
    def get_engines(self):
        return self.api.get_engines()
    
    @return_df
    def get_engine(self, engine: str):
        return self.api.get_engine(engine)
    
    @return_df
    def get_markets(self, engine: str):
        return self.api.get_markets(engine)
    
    @return_df
    def get_market(self, engine: str, market: str):
        return self.api.get_market(engine, market)
    
    @return_df
    def get_market_boards(self, engine: str, market: str):
        return self.api.get_market_boards(engine, market)
    
    @return_df
    def get_board(self, engine: str, market: str, board: str):
        return self.api.get_board(engine, market, board)

    @return_df
    def get_board_securities(self, engine: str, market: str, board: str):
        return self.api.get_board_securities(engine, market, board)
    
    @return_df
    def get_board_security(self, engine: str, market: str, board: str, security: str):
        return self.api.get_board_security(engine, market, board, security)
    
    @return_df
    def get_board_trades(self, engine: str, market: str, board: str, security: str):
        return self.api.get_board_trades(engine, market, board, security)
    
    @return_df
    def get_board_security_orderbook(self, engine: str, market: str, board: str, security: str):
        return self.api.get_board_security_orderbook(engine, market, board, security)
    
    @return_df
    def get_board_candles(self, engine: str, market: str, board: str, security: str):
        return self.api.get_board_candles(engine, market, board, security)
    
    @return_df
    def get_board_candleborders(self, engine: str, market: str, board: str, security: str):
        return self.api.get_board_candleborders(engine, market, board, security)
    
    @return_df
    def get_board_orderbook(self, engine: str, market: str, board: str):
        return self.api.get_board_orderbook(engine, market, board)
    
    @return_df
    def get_board_trades(self, engine: str, market: str, board: str):
        return self.api.get_board_trades(engine, market, board)
    
    
    # def get_board(self, engine: str, market: str, boards: str):
    #     """Получить описание режима торгов. Например: https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR.xml"""

    #     r = self.api.get(
    #         f"{self.endpoint}/{engine}/markets/{market}/boards/{boards}.{format}", # /iss/engines/[engine]/markets/[market]/boards/[board]
    #     )
        
    #     return self.api.
    

    # def get_board(self, engine: str, market: str, boards: str):
    #     """Получить описание режима торгов. Например: https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR.xml"""

    #     r = self.api.get(
    #         f"{self.endpoint}/{engine}/markets/{market}/boards/{boards}.{format}", # /iss/engines/[engine]/markets/[market]/boards/[board]
    #     )
        
    #     return self.api.
    

    # def get_board(self, engine: str, market: str, boards: str):
    #     """Получить описание режима торгов. Например: https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR.xml"""

    #     r = self.api.get(
    #         f"{self.endpoint}/{engine}/markets/{market}/boards/{boards}.{format}", # /iss/engines/[engine]/markets/[market]/boards/[board]
    #     )
        
    #     return self.api.
    

    # def get_board(self, engine: str, market: str, boards: str):
    #     """Получить описание режима торгов. Например: https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR.xml"""

    #     r = self.api.get(
    #         f"{self.endpoint}/{engine}/markets/{market}/boards/{boards}.{format}", # /iss/engines/[engine]/markets/[market]/boards/[board]
    #     )
        
    #     return self.api.
    

    # def get_board(self, engine: str, market: str, boards: str):
    #     """Получить описание режима торгов. Например: https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR.xml"""

    #     r = self.api.get(
    #         f"{self.endpoint}/{engine}/markets/{market}/boards/{boards}.{format}", # /iss/history/engines/[engine]/markets/[market]/boards/[board]/listing
    #     )
        
    #     return self.api.
    
    @return_df
    def get_market_boardgroups(self, engine: str, market: str):
        return self.api.get_market_boardgroups(engine, market)

    @return_df
    def get_boardgroup(self, engine: str, market: str, boardgroup: str):
        return self.api.get_boardgroup(engine, market, boardgroup)
    
    @return_df
    def get_boardgroup_candle(self, engine: str, market: str, boardgroup: str, security: str):
        return self.api.get_boardgroup_candle(engine, market, boardgroup, security)

    @return_df
    def get_boardgroup_candleborders(self, engine: str, market: str, boardgroup: str, security: str): 
        return self.api.get_boardgroup_candleborders(engine, market, boardgroup, security)
    
    @return_df
    def get_boardgroup_securities(self, engine: str, market: str, boardgroup: str):
        return self.api.get_boardgroup_securities(engine, market, boardgroup)
    
    @return_df
    def get_boardgroup_security(self, engine: str, market: str, boardgroup: str, security: str):
        return self.api.get_boardgroup_security(engine, market, boardgroup, security)
    
    @return_df
    def get_boardgroup_orderbook_by_security(self, engine: str, market: str, boardgroup: str, security: str):
        return self.api.get_boardgroup_orderbook_by_security(engine, market, boardgroup, security)
    
    @return_df
    def get_boardgroup_trades_by_security(self, engine: str, market: str, boardgroup: str, security: str):
        return self.api.get_boardgroup_trades_by_security(engine, market, boardgroup, security)
    
    @return_df
    def get_boardgroup_orderbook(self, engine: str, market: str, boardgroup: str):
        return self.api.get_boardgroup_orderbook(engine, market, boardgroup)
    
    @return_df
    def get_boardgroup_trades(self, engine: str, market: str, boardgroup: str):
        return self.api.get_boardgroup_trades(engine, market, boardgroup)

    @return_df
    def get_market_orderbook(self, engine: str, market: str):
        return self.api.get_market_orderbook(engine, market)
    
    @return_df
    def get_orderbook_columns(self, engine: str, market: str):        
        return self.api.get_orderbook_columns(engine, market)
    
    @return_df
    def get_market_trades(self, engine: str, market: str):
        return self.api.get_market_trades(engine, market)
    
    @return_df
    def get_trades_columns(self, engine: str, market: str):
        return self.api.get_trades_columns(engine, market)
    
    @return_df
    def get_market_turnovers(self, engine: str, market: str):
        return self.api.get_market_turnovers(engine, market)
    
    @return_df
    def get_secstats(self, engine: str, market: str):
        """
        Промежуточные "Итоги дня"
        Таблица заполняется после завершения соответствующей сессии.
        1 - Основная (дневная сессия)
        2 - Вечерняя сессия
        3 - Итого"""
        
        return self.api.get_secstats(engine, market)
    
    @return_df
    def get_turnovers(self, engine: str):
        return self.api.get_turnovers(engine)
    
    @return_df
    def get_all_zcyc(self, engine: str):
        return self.api.get_zcyc(engine)
    
    # TODO return data
    @return_df
    def get_zcyc(self, engine: str):
        return self.api.get_markets_zcyc(engine)
    
    @return_df
    def get_market_securities(self, engine: str, market: str):
        return self.api.get_market_securities(engine, market)
    
    @return_df
    def get_securities_columns(self, engine: str, market: str):
        return self.api.get_securities_columns(engine, market)
    
    @return_df
    def get_market_security(self, engine: str, market: str, security: str):
        return self.api.get_market_security(engine, market, security)
    
    @return_df
    def get_security_orderbook(self, engine: str, market: str, security: str):
        return self.api.get_security_orderbook(engine, market, security)
    
    @return_df
    def get_security_trades(self, engine: str, market: str, security: str):
        return self.api.get_security_trades(engine, market, security)
    
    @return_df
    def get_security_candles(self, engine: str, market: str, security: str):
        return self.api.get_security_candles(engine, market, security)
    
    @return_df
    def get_security_candleborders(self, engine: str, market: str, security: str):
        return self.api.get_security_candleborders(engine, market, security)
    
    @return_df
    def get_board(self, engine: str, market: str, boards: str):
        return self.api.get_board(engine, market, boards)
    
#     @return_df
#     def get_board(self, engine: str, market: str, boards: str):
#         """Получить описание режима торгов. Например: https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR.xml"""

#         r = self.api.get(
#             f"{self.endpoint}/{engine}/markets/{market}/boards/{boards}.{format}", # /iss/engines/[engine]/markets/[market]/boards/[board]
#         )
        
#         return self.api.
    
# @return_df
#     def get_board(self, engine: str, market: str, boards: str):
#         """Получить описание режима торгов. Например: https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR.xml"""

#         r = self.api.get(
#             f"{self.endpoint}/{engine}/markets/{market}/boards/{boards}.{format}", # /iss/engines/[engine]/markets/[market]/boards/[board]
#         )
        
#         return self.api.
    
# @return_df
#     def get_board(self, engine: str, market: str, boards: str):
#         """Получить описание режима торгов. Например: https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR.xml"""

#         r = self.api.get(
#             f"{self.endpoint}/{engine}/markets/{market}/boards/{boards}.{format}", # /iss/engines/[engine]/markets/[market]/boards/[board]
#         )
        
#         return self.api.
    
# @return_df
#     def get_board(self, engine: str, market: str, boards: str):
#         """Получить описание режима торгов. Например: https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR.xml"""

#         r = self.api.get(
#             f"{self.endpoint}/{engine}/markets/{market}/boards/{boards}.{format}", # /iss/engines/[engine]/markets/[market]/boards/[board]
#         )
        
#         return self.api.
    
# @return_df
#     def get_board(self, engine: str, market: str, boards: str):
#         """Получить описание режима торгов. Например: https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR.xml"""

#         r = self.api.get(
#             f"{self.endpoint}/{engine}/markets/{market}/boards/{boards}.{format}", # /iss/engines/[engine]/markets/[market]/boards/[board]
#         )
        
#         return self.api.
    
# @return_df
#     def get_board(self, engine: str, market: str, boards: str):
#         """Получить описание режима торгов. Например: https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR.xml"""

#         r = self.api.get(
#             f"{self.endpoint}/{engine}/markets/{market}/boards/{boards}.{format}", # /iss/engines/[engine]/markets/[market]/boards/[board]
#         )
        
#         return self.api.
    
# @return_df
#     def get_board(self, engine: str, market: str, boards: str):
#         """Получить описание режима торгов. Например: https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR.xml"""

#         r = self.api.get(
#             f"{self.endpoint}/{engine}/markets/{market}/boards/{boards}.{format}", # /iss/engines/[engine]/markets/[market]/boards/[board]
#         )
        
#         return self.api.
    
# @return_df
#     def get_board(self, engine: str, market: str, boards: str):
#         """Получить описание режима торгов. Например: https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR.xml"""

#         r = self.api.get(
#             f"{self.endpoint}/{engine}/markets/{market}/boards/{boards}.{format}", # /iss/engines/[engine]/markets/[market]/boards/[board]
#         )
        
#         return self.api.
    