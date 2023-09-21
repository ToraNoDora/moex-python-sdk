from typing import Optional
from pydantic import BaseModel

from moex_python_sdk.models import LangParams, RespData


# security groups
class SecurityGroupsParams(LangParams):
    hide_inactive: Optional[str] = "0"
    securitygroups: Optional[str] = ""
    trade_engine: Optional[str] = ""

def new_security_groups_params(
    lang: str = "ru",
    hide_inactive: str = None,
    securitygroups: str = None,
    trade_engine: str = None,
):
    return SecurityGroupsParams(
        lang=lang,
        hide_inactive=hide_inactive,
        securitygroups=securitygroups,
        trade_engine=trade_engine,
    )

class SecurityGroups(BaseModel):
    security_groups : RespData


# groups collections
class SecurityGroupsCollectionsParams(LangParams):
    ...

def new_security_groups_collections_params(lang: str = "ru"):
    return SecurityGroupsCollectionsParams(
        lang=lang,
    )

class SecurityGroupsCollections(BaseModel):
    collections: RespData

class SecurityGroupsCollection(BaseModel):
    collections: RespData
    boardgroups: RespData


# groups collection securities
class SecurityGroupsCollectionSecuritiesParams(SecurityGroupsCollectionsParams):
    start: str = "0"

def new_security_groups_collections_securities_params(lang: str = "ru", start: str = "0"):
    return SecurityGroupsCollectionSecuritiesParams(
        lang=lang,
        start=start,
    )

class SecurityGroupsCollectionSecurities(BaseModel):
    securities: RespData
    securities_cursor: RespData

