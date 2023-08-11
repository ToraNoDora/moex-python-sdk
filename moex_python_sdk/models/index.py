from typing import Optional
from pydantic import BaseModel

from moex_python_sdk.models import LangParams, RespData


# index
class IndexParams(LangParams):
    engine: Optional[str] # ! (for boardgroups || securitytypes)
    is_traded: Optional[str] = "0" # ! (for boardgroups) # Показывать только торгуемые группы режимов торгов, торгующиеся в настоящий момент: is_traded=1
    hide_inactive: Optional[str] = "0" # ! (for securitygroups)
    securitygroups: Optional[str] # ! (for securitygroups)
    trade_engine: Optional[str] # ! (for securitygroups)

def new_index_params(
        lang: str = "ru", 
        engine: str = None, 
        hide_inactive: str  = None,
        securitygroups: str = None, 
        trade_engine: str = None,
    ) -> IndexParams:
    return IndexParams(
        lang=lang,
        engine=engine,
        hide_inactive=hide_inactive,
        securitygroups=securitygroups,
        trade_engine=trade_engine,
    )

class Index(BaseModel):
    engines: RespData
    # Список доступных торговых систем
    markets: RespData
    # Справочник доступных рынков и их атрибуты.
    # Описание дополнительных полей:
    # - is_otc - Внебиржевой рынок.
    # - has_history_files - Формируются файлы с итогами торгов.
    # - has_history_trades_files - Формируются файлы с реестрами сделок.
    # - has_trades - Есть сделки внутри дня.
    # - has_history - Есть итоги торгов.
    # - has_candles - Для рынка есть свечки.
    # - has_orderbook - Есть стаканы заявок.
    # - has_tradingsession - Наличие дополнительных сессий у рынка.
    # - has_extra_yields - Для рынка рассчитываются дополнительные доходности.
    # - has_delay - Для рынка не предусмотрена задержка данных. 
    boards: RespData
    # Справочник режимов торгов 
    boardgroups: RespData
    # Справочник групп режимов торгов.
    # Расшифровка поля - "category" -> https://iss.moex.com/iss/index/handbooks/boardgroups_category.xml
    durations: RespData
    # Справочник доступных расчетных интервалов свечей в формате HLOCV
    securitytypes: RespData
    securitygroups: RespData
    securitycollections: RespData

# categories of boardgroups
class BoardgroupsCategories(BaseModel):
    handbooks_handbook: RespData

