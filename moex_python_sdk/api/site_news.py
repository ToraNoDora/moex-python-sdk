from moex_python_sdk.api._api import BaseApi
from moex_python_sdk.decorators import resp

from moex_python_sdk.models import new_resp_data
from moex_python_sdk.models.site_news import SiteNewsParams, SiteNews, SiteNew


@resp
class SiteNewsApi:
    def __init__(self, api: BaseApi):
        self.api = api
        self.endpoint = "/sitenews"

    def get_all_news(self, params: SiteNewsParams, format: str = "json"):
        """Новости биржи."""

        r = self.api.get(
            f"{self.endpoint}.{format}",
            params=params.as_dict(),
        )

        return r["url"], SiteNews(
            site_news=new_resp_data(r["data"]["sitenews"]),
            site_news_cursor=new_resp_data(r["data"]["sitenews.cursor"]),
        )

    def get_one_news(self, news_id: str, format: str = "json"):
        """Новость сайта."""

        r = self.api.get(
            f"{self.endpoint}/{news_id}.{format}",
        )

        return r["url"], SiteNew(content=new_resp_data(r["data"]["content"]))
