from typing import Optional

from pydantic import BaseModel

from moex_python_sdk.models import BaseParams, RespData


# years
class ArchiveYears(BaseModel):
    years: RespData


# period
class ArchivePeriodParams(BaseParams):
    year: Optional[str]
    month: Optional[str]
    format: Optional[str] = "json" # На какой формат данных отдавать ссылку: csv,json,xml

def new_period_params(years: str = None, month: str = None, format: str = "json") -> ArchivePeriodParams:
    return ArchivePeriodParams(
        years=years,
        month=month,
        format=format,
    )

class ArchivePeriod(BaseModel):
    files: RespData


# month
class ArchiveMonths(BaseModel):
    months: RespData

