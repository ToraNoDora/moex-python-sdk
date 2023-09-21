import random

from moex_python_sdk.api import MoexApi
from moex_python_sdk.models.events import new_events_params

from test.api import check_content


def test_events(moex_api: MoexApi):
    event_api = moex_api.event()

    params = new_events_params()
    events = event_api.get_events(params)["content"]

    check_content(events["events"])
    assert len(events["events"]["data"]) > 0

    _event = random.choice(events["events"]["data"])
    event = event_api.get_event(_event[0])

    check_content(event["content"]["content"])
    assert len(event["content"]["content"]) > 0
    assert _event[3] == event["content"]["content"]["data"][0][2]

