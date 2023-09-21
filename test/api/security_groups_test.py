from moex_python_sdk.api import MoexApi
from moex_python_sdk.models.security_groups import (
    new_security_groups_params,
    new_security_groups_collections_params,
    new_security_groups_collections_securities_params,
)

from test.api import check_content, check_all_content


def test_get_security_groups(
    moex_api: MoexApi,
    _security_group,
    _security_group_collection,
    _base_params,
):
    security_group_api = moex_api.security_group()

    params = new_security_groups_params()
    groups = security_group_api.get_security_groups(params)["content"]["security_groups"]

    check_content(groups)
    assert len(groups["data"]) > 0

    params = new_security_groups_params()
    group = security_group_api.get_security_group(
        _security_group,
        params,
    )["content"]["security_groups"]

    check_content(group)
    assert len(group["data"]) > 0

    params = new_security_groups_collections_params()
    collections = security_group_api.get_collections(
        _security_group,
        params,
    )["content"]["collections"]

    check_content(collections)
    assert len(collections["data"]) > 0

    collection = security_group_api.get_collection(
        _security_group,
        _security_group_collection,
        _base_params,
    )["content"]

    check_all_content(collection)

    params = new_security_groups_collections_securities_params()
    collection_securities = security_group_api.get_collection_securities(
        _security_group,
        _security_group_collection,
        params,
    )["content"]

    check_all_content(collection_securities)

