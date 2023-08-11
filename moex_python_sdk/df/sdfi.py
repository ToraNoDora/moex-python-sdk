from moex_python_sdk.api import MoexApi
from moex_python_sdk.decorators import return_df


class Sdfi:
    def __init__(self, api: MoexApi):
        self.api = api.sdfi()

    @return_df
    def get_curves(self):
        return self.api.get_curves()
    
    