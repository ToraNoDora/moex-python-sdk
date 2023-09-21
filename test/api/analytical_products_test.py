from moex_python_sdk.api import MoexApi
from moex_python_sdk.models.analytical_products import (
    new_curves_securities_params,
    new_futoi_securities_params,
    new_netflow2_securities_params,
)

from test.api import check_content


def test_get_analytical_products(moex_api: MoexApi):
    analytical_products_api = moex_api.analytical_product()

    params = new_curves_securities_params()
    curves = analytical_products_api.get_curves_securities(params)["content"]

    check_content(curves["curves"])
    assert len(curves["curves"]["data"]) > 0

    params = new_futoi_securities_params()
    futoi = analytical_products_api.get_futoi_securities(params)["content"]

    check_content(futoi["futoi"])
    assert len(futoi["futoi"]["data"]) > 0

    params = new_netflow2_securities_params()
    netflow2 = analytical_products_api.get_netflow2_securities(params)["content"]

    check_content(netflow2["netflow2"])
    assert len(netflow2["netflow2"]["data"]) > 0

