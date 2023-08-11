from pydantic import BaseModel

from moex_python_sdk.models import RespData


# sdfi
class SdfiCurvesParams(BaseModel):
    date: str = "today"

    def as_dict(self):
        return self.dict(exclude_none=True)

def new_sdfi_curves_params(date: str = "today"):
    return SdfiCurvesParams(
        date=date,
    )

class SdfiCurves(BaseModel):
    curves: RespData
