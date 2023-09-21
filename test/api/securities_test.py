import random

from moex_python_sdk.api import MoexApi
from moex_python_sdk.models.securities import (
    new_securities_params,
    new_security_params,
    new_security_indices_params,
)

from test.api import check_content, check_all_content


def test_get_securities(moex_api: MoexApi):
    security_api = moex_api.security()

    params = new_securities_params()
    securities = security_api.get_securities(params)["content"]["securities"]

    check_content(securities)
    assert len(securities["data"]) > 0

    _security = random.choice(securities["data"])[1]

    params = new_security_params()
    security = security_api.get_security(
        _security,
        params,
    )["content"]

    check_all_content(security)
    check_content(security["description"])
    assert len(security["description"]["data"]) > 0

    check_content(security["boards"])
    assert len(security["boards"]["data"]) > 0

    params = new_security_indices_params()
    security_indices = security_api.get_security_indices(
        _security,
        params,
    )["content"]

    check_content(security_indices["indices"])

