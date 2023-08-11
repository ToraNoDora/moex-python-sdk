from moex_python_sdk.api import MoexApi
from moex_python_sdk.decorators import return_df


class Event:
    def __init__(self, api: MoexApi):
        self.api = api.event()

    @return_df
    def get_events(self):
        return self.api.get_events()
    
    @return_df
    def get_event(self, event_id: str):
        return self.api.get_event(event_id)
    
    