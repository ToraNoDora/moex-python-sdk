from moex_python_sdk.api import MoexApi
from moex_python_sdk.decorators import return_df


class AnalyticalProduct:
    def __init__(self, api: MoexApi):
        self.api = api.analytical_product()

    @return_df
    def get_curves_securities(self):
        return self.api.get_curves_securities()
    
    @return_df
    def get_curves_security(self, security: str):
        return self.api.get_curves_security(security)
    
    @return_df
    def get_futoi_security(self):
        return self.api.get_futoi_securities()
    
    @return_df
    def get_futoi_security(self, security: str):
        return self.api.get_futoi_security(security)
    
    @return_df
    def get_netflow2_securities(self):
        return self.api.get_netflow2_securities()
    
    @return_df
    def get_netflow2_security(self, security: str):
        return self.api.get_netflow2_security(security)


    