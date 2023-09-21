from datetime import datetime

from moex_python_sdk.api import MoexApi

from test.api import check_content


def test_get_archives(moex_api: MoexApi, _engine):
    archive_api = moex_api.archive()

    list_by_years = archive_api.get_list_by_years(
        _engine,
        "index",
        "securities",
    )["content"]

    check_content(list_by_years["years"])
    assert len(list_by_years["years"]["data"]) > 0

    _current_year = datetime.now().year
    list_by_month = archive_api.get_list_by_month(
        _engine,
        "index",
        "securities",
        _current_year,
    )["content"]

    check_content(list_by_month["months"])
    assert len(list_by_month["months"]["data"]) > 0
