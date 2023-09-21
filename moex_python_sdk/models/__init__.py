from typing import Dict, List, Optional, Any
from pydantic import BaseModel


# resp
class Resp(BaseModel):
    url: str
    content: Any

class RespInfo(Resp):
    ...

def new_resp_info(url: str, content: Any):
    return RespInfo(url=url, content=content).model_dump(exclude_none=True)

class RespData(BaseModel):
    metadata: Dict
    columns: List
    data: List

def new_resp_data(data: Dict) -> RespData:
     if len(data) == 0:
          return None

     return RespData(
          metadata=data["metadata"],
          columns=data["columns"],
          data=data["data"],
     )


# Base params
class BaseParams(BaseModel):
    def as_dict(self, check: bool = False):
        params = self.model_dump(exclude_none=True)
        if check:
            return self._check(params)

        return params

    def _check(self, params: Dict):
        if "from_at" in params.keys():
            params["from"] = params["from_at"]
            params.pop("from_at", None)

        if "iss_reverse" in params.keys():
            params["iss.reverse"] = params["iss_reverse"]
            params.pop("iss_reverse", None)

        return {k:v for k, v in params.items() if v is not None}

class LangParams(BaseParams):
    lang: str = "ru" # ru || en

def new_lang_params(lang: str = "ru") -> LangParams:
    return LangParams(
        lang=lang,
    )


class DateParams(LangParams):
    date: Optional[str] = "today"

def new_date_params(lang: str = "ru", date: str = "today") -> DateParams:
    return DateParams(
        lang=lang,
        date=date,
    )


class MonthParams(LangParams):
    year: Optional[str]
    month: Optional[str]

def new_date_params(lang: str = "ru", year: str = None, month: str = None) -> MonthParams:
    return MonthParams(
        lang=lang,
        year=year,
        month=month,
    )


# proxy
class Proxy(BaseModel):
    http: Optional[str]
    https: Optional[str]

class User(BaseModel):
    username: str
    password: str

class MoexProxy(BaseModel):
    proxies: Optional[Proxy]
    user: User

def new_moex_proxy(username: str, password: str, http: str = None, https: str = None) -> MoexProxy:
     return MoexProxy(
          proxies=Proxy(
               http=http,
               https=https,
          ),
          user=User(
               username=username,
               password=password,
          ),
     )

