from moex_python_sdk.api import MoexApi
from moex_python_sdk.decorators import return_df


class Index:
    def __init__(self, api: MoexApi):
        self.api = api.index()

    @return_df
    def get_index(self):
        return self.api.get_index()
    
    