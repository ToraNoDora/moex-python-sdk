from typing import Optional
from pydantic import BaseModel

from moex_python_sdk.models import LangParams, RespData


# securities
class SecuritiesParams(LangParams):
    q: Optional[str]
    engine: Optional[str] = ""
    is_trading: Optional[str] = ""
    market: Optional[str] = ""
    group_by: Optional[str] = ""
    limit: str = "100"
    group_by_filter: Optional[str]
    start: int = 0

def new_securities_params(
    q: str = None,
    lang: str = "ru",
    engine: str = None,
    is_trading: str = None,
    market: str = None,
    group_by: str = None,
    limit: str = "100",
    group_by_filter: str = None,
    start: int = 0,
):
    return SecuritiesParams(
        q=q,
        lang=lang,
        engine=engine,
        is_trading=is_trading,
        market=market,
        group_by=group_by,
        limit=limit,
        group_by_filter=group_by_filter,
        start=start,
    )

class Securities(BaseModel):
    securities: RespData


class SecurityParams(LangParams):
    start: Optional[int] = 0

def new_security_params(lang: str = "ru", start:  int = None):
    return SecuritiesParams(
        lang=lang,
        start=start,
    )

class Security(BaseModel):
    description: RespData
    boards: RespData


# securities indices
class SecurityIndicesParams(LangParams):
    only_actual: str= "0"

def new_security_indices_params(lang: str = "ru", only_actual: str= "0"):
    return SecurityIndicesParams(
        lang=lang,
        only_actual=only_actual,
    )

class SecurityIndices(BaseModel):
    indices: RespData


# securities aggregates
class SecurityAggregatesParams(LangParams):
    date: str= "last"

def new_security_indices_params(lang: str = "ru", date: str= "0"):
    return SecurityAggregatesParams(
        lang=lang,
        date=date,
    )

class SecurityAggregates(BaseModel):
    aggregates: RespData
    agregates_dates: RespData

