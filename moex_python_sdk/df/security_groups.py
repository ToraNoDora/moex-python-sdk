from moex_python_sdk.api import MoexApi
from moex_python_sdk.decorators import return_df


class SecurityGroup:
    def __init__(self, api: MoexApi):
        self.api = api.security_group()

    @return_df
    def get_security_groups(self):
        return self.api.get_security_groups()
    
    @return_df
    def get_security_group(self, security_group: str):
        return self.api.get_security_group(security_group)
    
    @return_df
    def get_collections(self, security_group: str):
        return self.api.get_collections(security_group)
    
    @return_df
    def get_collection(self, security_group: str, collection: str):
        return self.api.get_collection(security_group, collection)
    
    @return_df
    def get_securities_collection(self, security_group: str, collection: str):
        return self.api.get_securities_collection(security_group, collection)
    
