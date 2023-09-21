import random

from moex_python_sdk.api import EngineApi

from test.api import check_content, check_all_content


def test_get_engines(engine_api: EngineApi, _engine, _base_params):
    engines = engine_api.get_engines(
        _base_params,
    )["content"]["engines"]

    check_content(engines)
    assert len(engines["data"]) > 0

    engine = engine_api.get_engine(
        _engine,
        _base_params,
    )["content"]

    check_all_content(engine)


def test_get_markets(engine_api: EngineApi, _engine, _market, _base_params):
    markets = engine_api.get_markets(
        _engine,
        _base_params,
    )["content"]["markets"]

    check_content(markets)
    assert len(markets["data"]) > 0

    market = engine_api.get_market(
        _engine,
        _market,
        _base_params,
    )["content"]

    check_content(market["boards"])
    assert len(market["boards"]["data"]) > 0

    check_content(market["board_groups"])
    assert len(market["board_groups"]["data"]) > 0

    check_content(market["securities"])
    assert len(market["securities"]["data"]) > 0

    check_content(market["market_data"])
    assert len(market["market_data"]["data"]) > 0

    check_content(market["trades"])
    assert len(market["trades"]["data"]) > 0

    check_content(market["trades_hist"])
    assert len(market["trades_hist"]["data"]) > 0

    check_content(market["orderbook"])
    assert len(market["orderbook"]["data"]) > 0

    check_content(market["history"])
    assert len(market["history"]["data"]) > 0

    check_content(market["secstats"])
    assert len(market["secstats"]["data"]) > 0


def test_get_market_boards(engine_api: EngineApi, _engine, _market, _board, _base_params):
    market_boards = engine_api.get_market_boards(
        _engine,
        _market,
        _base_params,
    )["content"]

    check_content(market_boards["boards"])
    assert len(market_boards["boards"]["data"]) > 0

    market_boards = engine_api.get_market_board(
        _engine,
        _market,
        _board,
        _base_params,
    )["content"]

    check_content(market_boards["board"])
    assert len(market_boards["board"]["data"]) > 0


def test_get_market_boardgroups(engine_api: EngineApi, _engine, _market, _base_params):
    market_boardgroups = engine_api.get_market_boardgroups(
        _engine,
        _market,
        _base_params,
    )["content"]["board_groups"]

    check_content(market_boardgroups)
    assert len(market_boardgroups["data"]) > 0

    _boardgroup = random.choice(market_boardgroups["data"])[1]
    market_boardgroup = engine_api.get_market_boardgroup(
        _engine,
        _market,
        _boardgroup,
        _base_params,
    )["content"]["board_group"]

    check_content(market_boardgroup)
    assert len(market_boardgroup["data"]) > 0

