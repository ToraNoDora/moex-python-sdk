from moex_python_sdk.api._api import BaseApi
from moex_python_sdk.decorators import resp

from moex_python_sdk.models import new_resp_data
from moex_python_sdk.models.site_news import SiteNewsParams, SiteNews, SiteNew


class SiteNewsApi:
    def __init__(self, api: BaseApi):
        self.api = api
        self.endpoint = "/sitenews"

    @resp
    def get_moex_news(self, params: SiteNewsParams, format: str = "json"):
        """Новости биржи."""

        r = self.api.get(
            f"{self.endpoint}.{format}", 
            params=params.as_dict(),
        )

        return r.url, SiteNews(
            sitenews=new_resp_data(r["sitenews"]),
            sitenews_cursor=new_resp_data(r["sitenews.cursor"]),
        )

    @resp
    def get_site_news(self, news_id: str, format: str = "json"):
        """Новость сайта."""

        r = self.api.get(
            f"{self.endpoint}/{news_id}.{format}", 
        )
        
        return r.url, SiteNew(content=new_resp_data(r["content"]))
    