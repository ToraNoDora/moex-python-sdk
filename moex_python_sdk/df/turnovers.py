from moex_python_sdk.api import MoexApi
from moex_python_sdk.decorators import return_df


class Turnover:
    def __init__(self, api: MoexApi):
        self.api = api.turnover()

    @return_df
    def get_turnovers(self):
        return self.api.get_turnovers()
    
    @return_df
    def get_turnovers_columns(self):
        return self.api.get_turnovers_columns()
    