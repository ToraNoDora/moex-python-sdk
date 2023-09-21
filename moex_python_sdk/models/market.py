from pydantic import BaseModel

from moex_python_sdk.models import RespData


class Markets(BaseModel):
    markets: RespData

