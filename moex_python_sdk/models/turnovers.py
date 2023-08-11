from pydantic import BaseModel

from moex_python_sdk.models import LangParams, RespData


# turnovers
class TurnoversParams(LangParams):
    is_tonight_session: str = "0"
    date: str = "today"
    
def new_turnovers_params(
    lang: str = "ru",
    is_tonight_session: str = "0",
    date: str = "today",
):
    return TurnoversParams(
        lang=lang,
        is_tonight_session=is_tonight_session,
        date=date,
    )

class Turnovers(BaseModel):
    turnovers: RespData
    turnoversprevdate: RespData # TODO
    
    
# turnovers columns
class TurnoversColumnsParams(LangParams):
    ...

def new_turnovers_columns_params(lang: str = "ru"):
    return TurnoversColumnsParams(
        lang=lang,
    )

class TurnoversColumns(BaseModel):
    turnovers: RespData

