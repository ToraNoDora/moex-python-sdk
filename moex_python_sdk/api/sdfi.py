from moex_python_sdk.api._api import BaseApi
from moex_python_sdk.decorators import resp

from moex_python_sdk.models import new_resp_data
from moex_python_sdk.models.sdfi import SdfiCurvesParams, SdfiCurves


class SdfiApi:
    def __init__(self, api: BaseApi):
        self.api = api
        self.endpoint = "/sdfi"

    @resp
    def get_curves(self, params: SdfiCurvesParams, format: str = "json"):
        """Своп-кривые на рынке СПФИ"""

        r = self.api.get(
            f"{self.endpoint}/curves/securities.{format}",
            params=params.as_dict(),
        )
        
        return r.url, SdfiCurves(curves=new_resp_data(r["curves"]))
    
    