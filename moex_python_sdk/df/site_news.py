from moex_python_sdk.api import MoexApi
from moex_python_sdk.decorators import return_df


class SiteNews:
    def __init__(self, api: MoexApi):
        self.api = api.site_news()

    @return_df
    def get_moex_news(self):
        return self.api.get_moex_news()

    @return_df
    def get_site_news(self, news_id: str):
        return self.api.get_site_news(news_id)
    