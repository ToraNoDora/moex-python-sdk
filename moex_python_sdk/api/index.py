from moex_python_sdk.api._api import BaseApi
from moex_python_sdk.decorators import resp

from moex_python_sdk.models import new_resp_data
from moex_python_sdk.models.index import IndexParams, Index, BoardgroupsCategories


@resp
class IndexApi:
    def __init__(self, api: BaseApi):
        self.api = api
        self.endpoint = "/index"

    def get_index(self, params: IndexParams, format: str = "json"):
        """Получить глобальные справочники ISS. Например: https://iss.moex.com/iss/index.xml."""

        r = self.api.get(
            f"{self.endpoint}.{format}",
            params=params.as_dict(),
        )

        return r["url"], Index(
            engines=new_resp_data(r["data"]["engines"]),
            markets=new_resp_data(r["data"]["markets"]),
            boards=new_resp_data(r["data"]["boards"]),
            board_groups=new_resp_data(r["data"]["boardgroups"]),
            durations=new_resp_data(r["data"]["durations"]),
            security_types=new_resp_data(r["data"]["securitytypes"]),
            security_groups=new_resp_data(r["data"]["securitygroups"]),
            security_collections=new_resp_data(r["data"]["securitycollections"]),
        )

    def get_boardgroups_categories(self, format: str = "json"):
        """Справочник групп режимов торгов."""

        r = self.api.get(
            f"{self.endpoint}/handbooks/boardgroups_category.{format}",
        )

        return r["url"], BoardgroupsCategories(handbooks_handbook=new_resp_data(r["data"]["handbooks_handbook"]))

