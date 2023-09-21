from pydantic import BaseModel

from moex_python_sdk.models import RespData


# boards
class BaseBoards(BaseModel):
    boards: RespData

class Boards(BaseBoards):
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