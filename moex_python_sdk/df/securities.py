from moex_python_sdk.api import MoexApi
from moex_python_sdk.decorators import return_df


class Security:
    def __init__(self, api: MoexApi):
        self.api = api.security()


    @return_df
    def get_securities(self):
        return self.api.get_securities()
    
    @return_df
    def get_security(self, security: str):
        return self.api.get_security(security)
    
    @return_df
    def get_security_indices(self, security: str):
        return self.api.get_security_indices(security)
    
    @return_df
    def get_security_aggregates(self, security: str):
        return self.api.get_security_aggregates(security)
    