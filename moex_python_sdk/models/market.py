from typing import Optional
from pydantic import BaseModel

from moex_python_sdk.models import LangParams, RespData


# markets
class Markets(BaseModel):
    markets: RespData

