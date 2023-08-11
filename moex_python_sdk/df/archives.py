from moex_python_sdk.api import MoexApi
from moex_python_sdk.decorators import return_df


class Arhive:
    def __init__(self, api: MoexApi):
        self.api = api.archive()

    @return_df
    def get_history_list_years(self, engine: str, market: str, datatype: str):
        return self.api.get_list_by_years(engine, market, datatype)
    
    @return_df
    def get_list_by_period(self, engine: str, market: str, datatype: str, period: str):
        return self.api.get_list_by_period(engine, market, datatype, period)
    
    @return_df
    def get_list_month(self, engine: str, market: str, datatype: str, year: str):
        return self.api.get_list_by_month(engine, market, datatype, year)
    