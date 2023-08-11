from typing import Optional
from pydantic import BaseModel

from moex_python_sdk.models import RespData


# analytical
class AnalyticalBase(BaseModel):
    date: Optional[str]


# curves
class CurvesParams(AnalyticalBase):
    time: Optional[str]

    def as_dict(self):
        return self.dict(exclude_none=True)
    
def new_curves_params(date: Optional[str] = None, time: Optional[str] = None) -> CurvesParams:
    return CurvesParams(
        date=date,
        time=time,
    )

class Curves(BaseModel):
    curves: RespData


class CurvesSecurityParams(BaseModel):
    till: Optional[str]
    from_at: Optional[str]

    def as_dict(self):
        params = self.dict(exclude_none=True)
        params["from"] = params["from_at"]
        params.pop("from_at", None)

        return {k:v for k, v in params.items() if v is not None}
    
def new_curves_security_params(till: str = None, from_at: str = None) -> CurvesSecurityParams:
    return CurvesSecurityParams(
        till=till,
        from_at=from_at,
    )


# futoi
class FutoiParams(AnalyticalBase):
    latest: Optional[str] # Последний срез за день ('1'-включить)
    table_type: Optional[str]

    def as_dict(self):
        return self.dict(exclude_none=True)
    
def new_futoi_params(
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


class FutoiSecurityParams(BaseModel):
    from_at: Optional[str]
    till: Optional[str]
    latest: Optional[str]

    def as_dict(self):
        params = self.dict(exclude_none=True)
        params["from"] = params["from_at"]
        params.pop("from_at", None)

        return {k:v for k, v in params.items() if v is not None}
    
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

    def as_dict(self):
        return self.dict(exclude_none=True)
    
def new_netflow2_params(date: Optional[str] = None) -> Netflow2Params:
    return Netflow2Params(
        date=date,
    )

class Netflow2(BaseModel):
    netflow2: RespData


class Netflow2SecurityParams(BaseModel):
    from_at: Optional[str]
    till: Optional[str]

    def as_dict(self):
        params = self.dict(exclude_none=True)
        params["from"] = params["from_at"]
        params.pop("from_at", None)

        return {k:v for k, v in params.items() if v is not None}
    
def new_netflow2_security_params(from_at: Optional[str] = None, till: Optional[str] = None) -> Netflow2SecurityParams:
    return Netflow2SecurityParams(
        from_at=from_at,
        till=till,
    )

