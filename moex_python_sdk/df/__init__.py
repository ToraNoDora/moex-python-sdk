from moex_python_sdk.api import MoexApi
from moex_python_sdk.df.analytical_products import AnalyticalProduct
from moex_python_sdk.df.archives import Arhive
from moex_python_sdk.df.engines import Engine
from moex_python_sdk.df.events import Event
from moex_python_sdk.df.history import History
from moex_python_sdk.df.index import Index
from moex_python_sdk.df.rms import Rms
from moex_python_sdk.df.sdfi import Sdfi
from moex_python_sdk.df.securities import Security
from moex_python_sdk.df.security_groups import SecurityGroup
from moex_python_sdk.df.site_news import SiteNews
from moex_python_sdk.df.statistics import Statistic
from moex_python_sdk.df.turnovers import Turnover


class MoexDataframe:
    """Изменяет данные полученные через api moex"""

    def __init__(self, moex: MoexApi):
        self._moex = moex

        self._prepare()

    def _prepare(self):
        self._analytical_product = AnalyticalProduct(self._moex)
        self._archive = Arhive(self._moex)
        self._engine = Engine(self._moex)
        self._event = Event(self._moex)
        self._history = History(self._moex)
        self._index = Index(self._moex)
        self._rms = Rms(self._moex)
        self._sdfi = Sdfi(self._moex)
        self._security = Security(self._moex)
        self._security_group = SecurityGroup(self._moex)
        self._site_news = SiteNews(self._moex)
        self._statistic = Statistic(self._moex)
        self._turnover = Turnover(self._moex)

    # ====== services ======
    def analytical_product(self) -> AnalyticalProduct:
        return self._analytical_product
        
    def archive(self) -> Arhive:
        return self._archive
    
    def engine(self) -> Engine:
        return self._engine
    
    def event(self) -> Event:
        return self._event
    
    def history(self) -> History:
        return self._history

    def index(self) -> Index:
        return self._index
    
    def rms(self) -> Rms:
        return self._rms

    def sdfi(self) -> Sdfi:
        return self._sdfi

    def security(self) -> Security:
        return self._security

    def security_group(self) -> SecurityGroup:
        return self._security_group

    def site_news(self) -> SiteNews:
        return self._site_news
    
    def statistic(self) -> Statistic:
        return self._statistic
    
    def turnover(self) -> Turnover:
        return self._turnover

    # ====== END services ======


__all__ = ["MoexDataframe"]

