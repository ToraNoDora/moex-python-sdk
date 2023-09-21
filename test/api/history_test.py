import random

from moex_python_sdk.api import HistoryApi
from moex_python_sdk.models.history import (
    new_history_dates_params,
    new_history_listing_params,
    new_history_dates_params,
    new_history_listing_params,
    new_history_total_securities_params,
    new_history_zcyc_params,
)

from test.api import check_content, check_all_content


def test_get_boards(history_api: HistoryApi, _engine, _market, _board):
    params = new_history_dates_params()
    board_by_dates = history_api.get_board_by_dates(
        _engine,
        _market,
        _board,
        params,
    )["content"]["dates"]

    check_content(board_by_dates)
    assert len(board_by_dates["data"]) > 0

    params = new_history_listing_params()
    board_listing = history_api.get_board_listing(
        _engine,
        _market,
        _board,
        params,
    )["content"]["securities"]

    check_content(board_listing)
    assert len(board_listing["data"]) > 0


def test_get_market(history_api: HistoryApi, _engine, _market, _base_params):
    params = new_history_dates_params()
    market_by_dates = history_api.get_market_by_dates(
        _engine,
        _market,
        params,
    )["content"]["dates"]

    check_content(market_by_dates)
    assert len(market_by_dates["data"]) > 0

    params = new_history_listing_params()
    market_by_listing = history_api.get_market_listing(
        _engine,
        _market,
        params,
    )["content"]["securities"]

    check_content(market_by_listing)
    assert len(market_by_listing["data"]) > 0

    listing_columns = history_api.get_listing_columns(
        _engine,
        _market,
        _base_params,
    )["content"]["securities"]

    check_content(listing_columns)
    assert len(listing_columns["data"]) > 0


def test_get_market_securities(history_api: HistoryApi, _engine, _market, _security, _base_params):
    securities_columns = history_api.get_securities_columns(
        _engine,
        _market,
        _base_params,
    )["content"]["history"]

    check_content(securities_columns)
    assert len(securities_columns["data"]) > 0

    params = new_history_dates_params()
    security_by_dates = history_api.get_security_by_dates(
        _engine,
        _market,
        _security,
        params,
    )["content"]["dates"]

    check_content(security_by_dates)
    assert len(security_by_dates["data"]) > 0

    market_sessions = history_api.get_market_sessions(
        _engine,
        _market,
        _base_params,
    )["content"]["trading_sessions"]

    check_content(market_sessions)
    assert len(market_sessions["data"]) > 0


def test_get_stock_totals(history_api: HistoryApi):
    boards = history_api.get_stock_totals_boards()["content"]["boards"]

    check_content(boards)
    assert len(boards["data"]) > 0

    _board = random.choice(boards["data"])[0]
    params = new_history_total_securities_params()
    board_by_securities = history_api.get_stock_totals_board_by_securities(
        _board,
        params,
    )["content"]["securities"]

    check_content(board_by_securities)
    assert len(board_by_securities["data"]) > 0

    params = new_history_total_securities_params()
    securities = history_api.get_stock_totals_securities(
        params,
    )["content"]

    check_all_content(securities)

    params = new_history_zcyc_params()
    zcyc = history_api.get_stock_zcyc(
        params,
    )["content"]["params"]

    check_content(zcyc)
    assert len(zcyc["data"]) > 0
