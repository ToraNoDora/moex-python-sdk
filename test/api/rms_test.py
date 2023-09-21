from moex_python_sdk.api import MoexApi
from moex_python_sdk.models.rms import (
    new_rms_object_params,
    new_settlements_calendar_params,
)

from test.api import check_content


def test_get_rms_objects(moex_api: MoexApi, _engine):
    rms_api = moex_api.rms()

    objects = rms_api.get_rms_objects(_engine)["content"]["objects"]

    check_content(objects)
    assert len(objects["data"]) > 0

    params = new_rms_object_params()
    limits = rms_api.get_rms_object_limits(
        _engine,
        params,
    )

    check_content(limits["content"]["limits"])
    assert len(limits["content"]["limits"]["data"]) > 0

    stat = rms_api.get_rms_object_stat(
        _engine,
        params,
    )

    check_content(stat["content"]["static_params"])
    assert len(stat["content"]["static_params"]["data"]) > 0

    market_rates = rms_api.get_rms_object_market_rates(
        _engine,
        params,
    )

    check_content(market_rates["content"]["market_rates"])
    assert len(market_rates["content"]["market_rates"]["data"]) > 0

    params = new_settlements_calendar_params()
    settlements_calendar = rms_api.get_object_settlements_calendar(
        _engine,
        params,
    )

    check_content(settlements_calendar["content"]["settlements_calendar"])
    assert len(settlements_calendar["content"]["settlements_calendar"]["data"]) > 0

