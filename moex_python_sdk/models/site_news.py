from pydantic import BaseModel

from moex_python_sdk.models import LangParams, RespData


# site news
class SiteNewsParams(LangParams):
    start: str = "0"
    
def new_security_groups_params(
    lang: str = "ru",
    start: str = "0",
):
    return SiteNewsParams(
        lang=lang,
        start=start,
    )

class SiteNews(BaseModel):
    sitenews: RespData
    sitenews_cursor: RespData
    

class SiteNew(BaseModel):
    content: RespData