from moex_python_sdk.api._api import BaseApi
from moex_python_sdk.decorators import resp

from moex_python_sdk.models import new_resp_data
from moex_python_sdk.models.events import EventsParams, Events, Event


class EventApi:
    def __init__(self, api: BaseApi):
        self.api = api
        self.endpoint = "/events"

    @resp
    def get_events(self, params: EventsParams, format: str = "json"):
        """Мероприятия биржи."""

        r = self.api.get(
            f"{self.endpoint}.{format}", 
            params=params.as_dict(),
        )

        return r.url, Events(
            events=new_resp_data(r["events"]),
            events_cursor=new_resp_data(r["events_cursor"]),
        )

    @resp
    def get_event(self, event_id: str, format: str = "json"):
        """Контент мероприятия биржи."""

        r = self.api.get(
            f"{self.endpoint}/{event_id}.{format}", 
        )

        return r.url, Event(content=new_resp_data(r["content"]))
    
    