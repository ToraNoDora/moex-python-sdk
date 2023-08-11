from typing import Optional

from pydantic import BaseModel

from moex_python_sdk.models import RespData


# years
class ArchiveYears(BaseModel):
    years: RespData


# period
class ArchivePeriodParams(BaseModel):
    year: Optional[str]
    month: Optional[str] # Фильтр по месяцу
    format: Optional[str] # На какой формат данных отдавать ссылку: csv,json,xml

    def as_dict(self):
        return self.dict(exclude_none=True)

def new_period_params(years: str, month: str, format: str) -> ArchivePeriodParams:
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

