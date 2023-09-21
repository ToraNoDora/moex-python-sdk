from moex_python_sdk.api import MoexApi
from moex_python_sdk.models.turnovers import (
    new_turnovers_params,
    new_turnovers_columns_params,
)

from test.api import check_content, check_all_content


def test_get_turnovers(moex_api: MoexApi):
    security_group_api = moex_api.turnover()

    params = new_turnovers_params()
    turnovers = security_group_api.get_turnovers(params)["content"]

    check_all_content(turnovers)

    params = new_turnovers_columns_params()
    turnover = security_group_api.get_turnovers_columns(
        params,
    )["content"]["turnovers"]

    check_content(turnover)
    assert len(turnover["data"]) > 0

