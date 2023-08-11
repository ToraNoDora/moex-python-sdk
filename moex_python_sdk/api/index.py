from moex_python_sdk.api._api import BaseApi
from moex_python_sdk.decorators import resp

from moex_python_sdk.models import new_resp_data
from moex_python_sdk.models.index import IndexParams, Index, BoardgroupsCategories


class IndexApi:
    def __init__(self, api: BaseApi):
        self.api = api
        self.endpoint = "/index"

    @resp
    def get_index(self, params: IndexParams, format: str = "json"):
        """Получить глобальные справочники ISS. Например: https://iss.moex.com/iss/index.xml."""

        r = self.api.get(
            f"{self.endpoint}.{format}", 
            params=params.as_dict(),
        )

        return r.url, Index(
            engines=new_resp_data(r["engines"]),
            markets=new_resp_data(r["markets"]), 
            boards=new_resp_data(r["boards"]), 
            boardgroups=new_resp_data(r["boardgroups"]), 
            durations=new_resp_data(r["durations"]), 
            securitytypes=new_resp_data(r["securitytypes"]), 
            securitygroups=new_resp_data(r["securitygroups"]), 
            securitycollections=new_resp_data(r["securitycollections"]),
        )

    @resp
    def get_boardgroups_categories(self, format: str = "json"):
        """Справочник групп режимов торгов."""

        r = self.api.get(
            f"{self.endpoint}/handbooks/boardgroups_category.{format}", 
        )

        return r.url, BoardgroupsCategories(handbooks_handbook=new_resp_data(r["handbooks_handbook"]))
    
