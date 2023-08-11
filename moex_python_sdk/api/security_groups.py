from moex_python_sdk.api._api import BaseApi
from moex_python_sdk.decorators import resp

from moex_python_sdk.models import new_resp_data
from moex_python_sdk.models.security_groups import (
    SecurityGroupsParams,
    SecurityGroups, 
    SecurityGroupsCollectionsParams,
    SecurityGroupsCollections, 
    SecurityGroupsCollection, 
    SecurityGroupsCollectionSecuritiesParams,
    SecurityGroupsCollectionSecurities,
)


class SecurityGroupApi:
    def __init__(self, api: BaseApi):
        self.api = api
        self.endpoint = "/securitygroups"

    @resp
    def get_security_groups(self, params: SecurityGroupsParams, format: str = "json"):
        """Группы ценных бумаг."""

        r = self.api.get(
            f"{self.endpoint}.{format}", 
            params=params.as_dict(),
        )

        return r.url, SecurityGroups(security_groups=new_resp_data(r["securitygroups"]))

    @resp
    def get_security_group(self, security_group: str, params: SecurityGroupsParams, format: str = "json"):
        """Группа ценных бумаг."""

        r = self.api.get(
            f"{self.endpoint}/{security_group}.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, SecurityGroupsCollections(collections=new_resp_data(r["collections"]))

    @resp
    def get_collections(self, security_group: str, params: SecurityGroupsCollectionsParams, format: str = "json"):
        """Коллекции ценных бумаг входящие в группу."""

        r = self.api.get(
            f"{self.endpoint}/{security_group}/collections.{format}", 
            params=params.as_dict(),
        )
        
        return r.url, SecurityGroupsCollections(collections=new_resp_data(r["collections"]))

    @resp
    def get_collection(self, security_group: str, collection: str, params: SecurityGroupsCollectionsParams, format: str = "json"):
        """Коллекция ценных бумаг входящие в группу."""

        r = self.api.get(
            f"{self.endpoint}/{security_group}/collections/{collection}.{format}", 
            params=params.as_dict,
        )
        
        return r.url, SecurityGroupsCollection(
            collections=new_resp_data(r["collections"]),
            boardgroups=new_resp_data(r["boardgroups"]),
        )

    @resp
    def get_securities_collection(self, security_group: str, collection: str, params: SecurityGroupsCollectionSecuritiesParams, format: str = "json"):
        """Описание инструментов."""

        r = self.api.get(
            f"{self.endpoint}/{security_group}/collections/{collection}/securities.{format}",
            params=params.as_dict(),
        )
        
        return r.url, SecurityGroupsCollectionSecurities(
            securities=new_resp_data(r["securities"]),
            securities_cursor=new_resp_data(r["securities.cursor"]),
        )
    
