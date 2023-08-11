from moex_python_sdk.api._api import BaseApi
from moex_python_sdk.decorators import resp

from moex_python_sdk.models import new_resp_data
from moex_python_sdk.models.turnovers import TurnoversParams, Turnovers, TurnoversColumnsParams, TurnoversColumns


class TurnoverApi:
    def __init__(self, api: BaseApi):
        self.api = api
        self.endpoint = "/turnovers"

    @resp
    def get_turnovers(self, params: TurnoversParams, format: str = "json"):
        """Получить сводные обороты по рынкам. Например: https://iss.moex.com/iss/turnovers.xml."""

        r = self.api.get(
            f"{self.endpoint}.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, Turnovers(
            turnovers=new_resp_data(r["turnovers"]),
            turnoversprevdate=new_resp_data(r["turnoversprevdate"])
        )

    @resp
    def get_turnovers_columns(self, params: TurnoversColumnsParams, format: str = "json"):
        """Получить описание полей для запросов оборотов по рынку/торговой системе. Например: https://iss.moex.com/iss/engines/stock/turnovers/columns.xml"""

        r = self.api.get(
            f"{self.endpoint}/columns.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, TurnoversColumns(turnovers=new_resp_data(r["turnovers"]))
    
    