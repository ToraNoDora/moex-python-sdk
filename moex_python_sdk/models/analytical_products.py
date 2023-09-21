from typing import Optional
from pydantic import BaseModel

from moex_python_sdk.models import BaseParams, RespData


# analytical
class AnalyticalBase(BaseParams):
    date: Optional[str]


# curves
class CurvesParams(AnalyticalBase):
    time: Optional[str]

def new_curves_securities_params(date: Optional[str] = None, time: Optional[str] = None) -> CurvesParams:
    return CurvesParams(
        date=date,
        time=time,
    )

class Curves(BaseModel):
    curves: RespData


class CurvesSecurityParams(BaseParams):
    till: Optional[str]
    from_at: Optional[str]

def new_curves_security_params(till: str = None, from_at: str = None) -> CurvesSecurityParams:
    return CurvesSecurityParams(
        till=till,
        from_at=from_at,
    )


# futoi
class FutoiParams(AnalyticalBase):
    latest: Optional[str] # Последний срез за день ('1'-включить)
    table_type: Optional[str]

def new_futoi_securities_params(
        date: Optional[str] = None,
        latest: Optional[str] = None,
        table_type: Optional[str] = None,
    ) -> FutoiParams:
    return FutoiParams(
        date=date,
        latest=latest,
        table_type=table_type,
    )

class Futoi(BaseModel):
    futoi: RespData
    futoi_dates: RespData


class FutoiSecurityParams(BaseParams):
    from_at: Optional[str]
    till: Optional[str]
    latest: Optional[str]

def new_futoi_security_params(
        from_at: Optional[str] = None,
        till: Optional[str] = None,
        latest: Optional[str] = None,
    ) -> FutoiSecurityParams:
    return FutoiSecurityParams(
        from_at=from_at,
        till=till,
        latest=latest,
    )


# netflow2
class Netflow2Params(AnalyticalBase):
    ...

def new_netflow2_securities_params(date: Optional[str] = None) -> Netflow2Params:
    return Netflow2Params(
        date=date,
    )

class Netflow2(BaseModel):
    netflow2: RespData


class Netflow2SecurityParams(BaseParams):
    from_at: Optional[str]
    till: Optional[str]

def new_netflow2_security_params(from_at: Optional[str] = None, till: Optional[str] = None) -> Netflow2SecurityParams:
    return Netflow2SecurityParams(
        from_at=from_at,
        till=till,
    )

