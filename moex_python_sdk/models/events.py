from typing import Optional
from pydantic import BaseModel

from moex_python_sdk.models import LangParams, RespData


# events
class EventsParams(LangParams):
    start: Optional[str] = "0"

def new_events_params(lang: str = "ru", start: str = "0") -> EventsParams:
    return EventsParams(
        lang=lang,
        start=start,
    )

class Events(BaseModel):
    events: RespData
    events_cursor: RespData


class Event(BaseModel):
    content: RespData

