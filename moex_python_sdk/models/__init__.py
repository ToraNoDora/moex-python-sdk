from typing import Dict, List, Optional, Any
from pydantic import BaseModel


# resp
class Resp(BaseModel):
    url: str
    content: Any

class RespInfo(Resp):
    ...

def new_resp_info(url: str, content: Any):
    return RespInfo(url=url, content=content).dict(exclude_none=True)
    # return RespInfo(url=url, content=content)

class RespData(BaseModel):
    metadata: Dict
    columns: List
    data: List

def new_resp_data(data: Dict) -> RespData:
     if not data:
          return None

     return RespData(
          metadata=data["metadata"],
          columns=data["columns"],
          data=data["data"],
     )


# Base params
class BaseParams(BaseModel):
#     lang: str = "ru" # ru || en

    def as_dict(self):
        return self.dict(exclude=True)


class LangParams(BaseParams):
     lang: str = "ru" # ru || en

def new_lang_params(lang: str = "ru", date: str = "today") -> LangParams:
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


from requests import Session
from requests.auth import HTTPProxyAuth


def connection_with_proxy(session: Session, proxy: MoexProxy):
        print(proxy)

        auth = HTTPProxyAuth(proxy.user.username, proxy.user.password)
        session.proxies = proxy.proxies.dict()
        session.auth = auth        # Set authorization parameters globally

        # ext_ip = session.get('http://iss.moex.com/iss', proxies=proxy.proxies.dict(), verify=False)
        # ext_ip = session.get("http://10.36.41.178:5556/iss", verify=False)
        # # print("is_redirect: ", ext_ip.next.url)
        # print(ext_ip.url)
        # print(ext_ip.text)


session = Session()

connection_with_proxy(
     session=session,
     proxy=MoexProxy(
          proxies=Proxy(
               http="http://nsproxy1.rosbank.rus.socgen:8080",
               https="https://nsproxy1.rosbank.rus.socgen:8080",
          ),
          user=User(
               username="",
               password="",
          ),
     ))


