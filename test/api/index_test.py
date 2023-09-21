from moex_python_sdk.api import MoexApi
from moex_python_sdk.models.index import new_index_params

from test.api import check_all_content


def test_get_index(moex_api: MoexApi):
    index_api = moex_api.index()

    params = new_index_params()
    index = index_api.get_index(params)["content"]

    check_all_content(index)

