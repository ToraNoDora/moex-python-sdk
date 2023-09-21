from typing import Dict

from pytest import fixture

from moex_python_sdk import Moex
from moex_python_sdk.models import new_lang_params


# base api
@fixture
def base_moex_url():
    return "https://iss.moex.com"

@fixture
def moex_api(base_moex_url):
    return Moex(
        base_url=base_moex_url,
        warnings=False,
    ).api()

@fixture
def engine_api(moex_api):
    return moex_api.engine()

@fixture
def history_api(moex_api):
    return moex_api.history()


# base value
@fixture
def _base_params():
    return new_lang_params()

@fixture
def _value_() -> Dict:
    return {
        "engine": "stock",
        "market": "shares",
        "board": "TQBR",
        "boardgroup": "stock_etf_usd",
        "security": "AF10000BF4",
        "security_group": "currency_futures",
        "security_group_collection": "currency_futures_delivery_eur",
    }

@fixture
def _engine(_value_: Dict):
    return _value_.get("engine")

@fixture
def _market(_value_: Dict):
    return _value_.get("market")

@fixture
def _boardgroup(_value_: Dict):
    return _value_.get("boardgroup")

@fixture
def _board(_value_: Dict):
    return _value_.get("board")

@fixture
def _security(_value_: Dict):
    return _value_.get("security")

@fixture
def _security_group(_value_: Dict):
    return _value_.get("security_group")

@fixture
def _security_group_collection(_value_: Dict):
    return _value_.get("security_group_collection")


