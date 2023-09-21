from pydantic import BaseModel

from moex_python_sdk.models import LangParams, RespData


# site news
class SiteNewsParams(LangParams):
    start: str = "0"

def new_site_news_params(
    lang: str = "ru",
    start: str = "0",
):
    return SiteNewsParams(
        lang=lang,
        start=start,
    )

class SiteNews(BaseModel):
    site_news: RespData
    site_news_cursor: RespData


class SiteNew(BaseModel):
    content: RespData