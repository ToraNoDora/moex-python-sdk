from moex_python_sdk.api._api import BaseApi

from moex_python_sdk.api.analytical_products import AnalyticalProductApi
from moex_python_sdk.api.archives import ArhiveApi
from moex_python_sdk.api.engines import EngineApi
from moex_python_sdk.api.events import EventApi
from moex_python_sdk.api.history import HistoryApi
from moex_python_sdk.api.index import IndexApi
from moex_python_sdk.api.rms import RmsApi
from moex_python_sdk.api.securities import SecurityApi
from moex_python_sdk.api.security_groups import SecurityGroupApi
from moex_python_sdk.api.site_news import SiteNewsApi
from moex_python_sdk.api.statistics import StatisticApi
from moex_python_sdk.api.turnovers import TurnoverApi


class MoexApi:
    """Предоставляет доступ к api moex"""

    def __init__(self, api: BaseApi):
        self.api = api

        self._prepare_api()

    def _prepare_api(self):
        self._analytical_product_api = AnalyticalProductApi(self.api)
        self._archive_api = ArhiveApi(self.api)
        self._engine_api = EngineApi(self.api)
        self._event_api = EventApi(self.api)
        self._history_api = HistoryApi(self.api)
        self._index_api = IndexApi(self.api)
        self._rms_api = RmsApi(self.api)
        self._security_api = SecurityApi(self.api)
        self._security_group_api = SecurityGroupApi(self.api)
        self._site_news_api = SiteNewsApi(self.api)
        self._statistic_api = StatisticApi(self.api)
        self._turnover_api = TurnoverApi(self.api)

    # ====== APIs ======
    def analytical_product(self) -> AnalyticalProductApi:
        return self._analytical_product_api

    def archive(self) -> ArhiveApi:
        return self._archive_api

    def engine(self) -> EngineApi:
        return self._engine_api

    def event(self) -> EventApi:
        return self._event_api

    def history(self) -> HistoryApi:
        return self._history_api

    def index(self) -> IndexApi:
        return self._index_api

    def rms(self) -> RmsApi:
        return self._rms_api

    def security(self) -> SecurityApi:
        return self._security_api

    def security_group(self) -> SecurityGroupApi:
        return self._security_group_api

    def site_news(self) -> SiteNewsApi:
        return self._site_news_api

    def statistic(self) -> StatisticApi:
        return self._statistic_api

    def turnover(self) -> TurnoverApi:
        return self._turnover_api

    # ====== END APIs ======


__all__ = ["MoexApi", "BaseApi"]

