from typing import Optional

from pydantic import BaseModel

from moex_python_sdk.models import LangParams, RespData
from moex_python_sdk.models.securities import Securities


# statistic rates
class StatisticRates(BaseModel):
    auctions: RespData
    fixed: RespData
    

# statistic rates columns
class StatisticRatesColumns(BaseModel):
    columns: RespData
    


# statistic derivatives report
class StatisticDerivativesReportParams(LangParams):
    date: Optional[str] = "latest"
    
def new_derivatives_report_params(date: str = "latest") -> StatisticDerivativesReportParams:
    return StatisticDerivativesReportParams(
        date=date,
    )

class StatisticDerivativesReport(BaseModel):
    columns: RespData
    data: RespData


#
class StatisticFixingParams(LangParams):
    from_at: Optional[str] = "1997-01-01"
    till: Optional[str] = "2100-12-31"
    limit: Optional[str] = "100"
    sort_order: Optional[str] = "asc"
    
    def as_dict(self):
        params = self.dict(exclude_none=True)
        if params["from_at"]:
            params["from"] = params["from_at"]
            params.pop("from_at", None)

        return {k:v for k, v in params.items() if v is not None}
    
def new_statistic_fixing_params(
        from_at: str = "1997-01-01",
        till: str = "2100-12-31",
        limit: str = "100",
        sort_order: str = "asc",
) -> StatisticFixingParams:
    return StatisticFixingParams(
        from_at=from_at,
        till=till,
        limit=limit,
        sort_order=sort_order,
    )

class StatisticFixing(BaseModel):
    history: RespData
    history_cursor: RespData
    history_dates:  RespData


# 
class IndicativeratesSecuritiesParams(LangParams):
    date: Optional[str] = "today"
    lang: Optional[str] = "ru"
    clearing: Optional[str] # Показывать данные только для соответсвующуго клиринга.
    # "pk" - Промежуточный (дневной) клиринг.
    # "vk" - Вечерний (основной) клиринг.
    
def new_indicativerates_securities_params(
        date: str = "today",
        lang: str = None,
        clearing: str = None,
) -> StatisticFixingParams:
    return StatisticFixingParams(
        date=date,
        lang=lang,
        clearing=clearing,
    )

class IndicativeratesSecurities(Securities):
    securities_list: RespData


#
class IndicativeratesSecurityParams(LangParams):
    from_at: Optional[str] = "1997-01-01"
    till: Optional[str] = "2100-12-31"
    limit: Optional[str] = "100"
    sort_order: Optional[str] = "asc"
    start: Optional[str] = "0"
    
    def as_dict(self):
        params = self.dict(exclude_none=True)
        if params["from_at"]:
            params["from"] = params["from_at"]
            params.pop("from_at", None)

        return {k:v for k, v in params.items() if v is not None}
    
def new_statistic_fixing_params(
        from_at: str = "1997-01-01",
        till: str = "2100-12-31",
        limit: str = "100",
        sort_order: str = "asc",
        start: str = "0",
) -> IndicativeratesSecurityParams:
    return IndicativeratesSecurityParams(
        from_at=from_at,
        till=till,
        limit=limit,
        sort_order=sort_order,
        start=start,
    )

class IndicativeratesSecurity(Securities):
    securities_cursor: RespData
    securities_dates: RespData
    securities_current: RespData


# 
class StatisticMarketParams(BaseModel):
    date: Optional[str] = "today"

    def as_dict(self):
        return self.dict(exclude_none=True)

class MarketsFixingParams(LangParams, StatisticMarketParams):
    ...
    
def new_markets_fixing_params(
        lang: str = "ru",
        date: str = "today",
) -> MarketsFixingParams:
    return MarketsFixingParams(
        lang=lang,
        date=date,
    )

class MarketsFixing(Securities):
    history: RespData
    history_dates: RespData


#
class MarketsSecurityParams(LangParams, StatisticMarketParams):
    from_at: Optional[str]
    till: Optional[str] 
    limit: Optional[str] = "20"
    
    def as_dict(self):
        params = self.dict(exclude_none=True)
        if params["from_at"]:
            params["from"] = params["from_at"]
            params.pop("from_at", None)

        return {k:v for k, v in params.items() if v is not None}
    
def new_markets_security_params(
        from_at: str = None,
        till: str = None,
        limit: str = "20",
) -> MarketsSecurityParams:
    return MarketsSecurityParams(
        from_at=from_at,
        till=till,
        limit=limit,
    )


#
class StatisticsAssetsParams(LangParams):
    date: Optional[str] = "today"
    asset_type: Optional[str] # Фильтр по типу базового актива. (S - Опционы на акцию)
    limit: Optional[str] = "20"
    
def new_assets_params(
        from_at: str = None,
        till: str = None,
        limit: str = "20",
) -> StatisticsAssetsParams:
    return StatisticsAssetsParams(
        from_at=from_at,
        till=till,
        limit=limit,
    )

class StatisticsAssets(BaseModel):
    asset_volumes: RespData

# 
class StatisticsAsset(BaseModel):
    expirations: RespData


# 
class AssetOptionboardParams(BaseModel):
    expiration_date: Optional[str] # Дата исполнения контракта
    
    def as_dict(self):
        return self.dict(exclude_none=True)
    
def new_asset_optionboard_params(
        expiration_date: str = None,
) -> AssetOptionboardParams:
    return AssetOptionboardParams(
        expiration_date=expiration_date,
    )

class AssetOptionboar(BaseModel):
    call: RespData
    put: RespData
    asset: RespData 


# 
class AssetOpenpositionsParams(BaseModel):
    date: Optional[str] = "today" # Дата исполнения контракта
    asset_type: Optional[str] = "S" # Фильтр по типу базового актива. (S - Опционы на акцию, F - Опционы на фьючерс)
    option_type: Optional[str] = "C" # Тип опциона: 'C' - Call, 'P' - Put.
    
    def as_dict(self):
        return self.dict(exclude_none=True)
    
def new_asset_openpositions_params(
        date: str = "today",
        asset_type: str = "S",
        option_type: str = "C",
) -> AssetOpenpositionsParams:
    return AssetOpenpositionsParams(
        date=date,
        asset_type=asset_type,
        option_type=option_type,
    )

class AssetOpenpositions(BaseModel):
    open_positions: RespData


# 
class AssetTurnoversParams(BaseModel):
    series_type: Optional[str] 
    
    def as_dict(self):
        return self.dict(exclude_none=True)
    
def new_asset_turnovers_params(
        series_type: str = None,
) -> AssetTurnoversParams:
    return AssetTurnoversParams(
        series_type=series_type,
    )

class AssetTurnovers(BaseModel):
    asset_turnovers: RespData


# complex
class ComplexSecuritiesParams(BaseModel):
    start: Optional[str] = "0"
    
    def as_dict(self):
        return self.dict(exclude_none=True)
    
def new_complex_securities_params(
        start: str = "0",
) -> ComplexSecuritiesParams:
    return ComplexSecuritiesParams(
        start=start,
    )


class ComplexSecurity(Securities):
    security_columns: RespData


# correlations
class SharesCorrelationsParams(BaseModel):
    date: Optional[str] = "today"
    start: Optional[int] = 0
    
    def as_dict(self):
        return self.dict(exclude_none=True)
    
def new_shares_correlations_params(
        date: str = "0",
        start: int = 0,
) -> SharesCorrelationsParams:
    return SharesCorrelationsParams(
        date=date,
        start=start,
    )

class SharesCorrelations(BaseModel):
    coefficients: RespData
    coefficients_cursor: RespData
    coefficients_dates: RespData


# cbrf 
class CbrfParams(BaseModel):
    date: Optional[str] = "today"
    
    def as_dict(self):
        return self.dict(exclude_none=True)
    
def new_cbrf_params(
        date: str = None,
) -> CbrfParams:
    return CbrfParams(
        date=date,
    )

class Cbrf(BaseModel):
    cbrf: RespData
    wap_rates: RespData


# splits
class Splits(BaseModel):
    splits: RespData


# mirp
class MirpParams(LangParams):
    date: Optional[str] = "today"
    sort_order: Optional[str] = "emitent" # Поле, по которому сортируется ответ.
    sort_order_desc: Optional[str] = "emitent"
    start: Optional[int] = 0 

def new_mirp_params(
        lang: str = None,
        date: str = None,
) -> MirpParams:
    return MirpParams(
        lang=lang,
        date=date,
    )

class Mirp(BaseModel):
    data: RespData
    data_cursor: RespData
    data_dates: RespData


# dealers
class DealersParams(LangParams):
    date: Optional[str] = "today"

def new_dealers_params(
        lang: str = None,
        date: str = None,
) -> DealersParams:
    return DealersParams(
        lang=lang,
        date=date,
    )

class Dealers(BaseModel):
    data: RespData
    data_dates: RespData


# cboper
class CboperParams(LangParams):
    date: Optional[str] = "today"

def new_cboper_params(
        lang: str = None,
        date: str = None,
) -> CboperParams:
    return CboperParams(
        lang=lang,
        date=date,
    )

class Cboper(BaseModel):
    date: RespData
    dates: RespData


# deviationcoeffs
class DeviationcoeffsParams(BaseModel):
    date: Optional[str] = "today"
    start: Optional[int] = 0

    def as_dict(self):
        return self.dict(exclude_none=True)
    
def new_deviationcoeffs_params(
        date: str = "today",
        start: int = 0,
) -> DeviationcoeffsParams:
    return DeviationcoeffsParams(
        start=start,
        date=date,
    )

class Deviationcoeffs(BaseModel):
    securities: RespData
    securities_cursor: RespData
    securities_dates: RespData


# quotedsecurities
class QuotedSecuritiesParams(BaseModel):
    date: Optional[str] = "today"

    def as_dict(self):
        return self.dict(exclude_none=True)
    
def new_quoted_securities_params(
        date: str = "today",
) -> QuotedSecuritiesParams:
    return QuotedSecuritiesParams(
        date=date,
    )

class QuotedSecurities(BaseModel):
    quotedsecurities: RespData
    quotedsecurities_dates: RespData


# current prices
class CurrentPricesParams(BaseModel):
    date: Optional[str] = "today"
    start: Optional[int] = 0
    tradingsession: Optional[str] # Фильтровать по типу торговой сессии:
    # 1 - Утренняя сессия
    # 1 - Основная сессия
    # 2 - Вечерняя сессия
    # 3 - Суммарно по всем сессиям
    # По умолчанию показываются все сессии.  

    def as_dict(self):
        return self.dict(exclude_none=True)
    
def new_current_prices_params(
        date: str = "today",
        start: int = 0,
        tradingsession: str = None, 
) -> CurrentPricesParams:
    return CurrentPricesParams(
        date=date,
        start=start,
        tradingsession=tradingsession,
    )

class CurrentPrices(BaseModel):
    currentprices: RespData
    currentprices_dates: RespData


# monthendaccints
class MonthendaccintsParams(BaseModel):
    date: Optional[str] = "today"  

    def as_dict(self):
        return self.dict(exclude_none=True)
    
def new_monthendaccints_params(
        date: str = "today",
) -> MonthendaccintsParams:
    return MonthendaccintsParams(
        date=date,
    )
    
class Monthendaccints(BaseModel):
    monthend_accints: RespData
    monthend_accints_index: RespData


# analytics columns
class AnalyticsColumns(BaseModel):
    analytics_columns: RespData


# bulletins 
class BulletinsParams(BaseModel):
    date: Optional[str] = "today"  
    market: Optional[str] # Рынок
    # EQ - индекс акций
    # FI - индекс облигаций
    # MX - составные индексы

    def as_dict(self):
        return self.dict(exclude_none=True)
    
def new_bulletins_params(
        date: str = "today",
        market: str = None,
) -> BulletinsParams:
    return BulletinsParams(
        date=date,
        market=market,
    )
    
class Bulletins(BaseModel):
    bulletins: RespData


# rusfar
class RusfarParams(BaseModel):
    date: Optional[str] = "today"

    def as_dict(self):
        return self.dict(exclude_none=True)
    
def new_rusfar_params(
        date: str = None,
) -> RusfarParams:
    return RusfarParams(
        date=date,
    )
    
class Rusfar(BaseModel):
    analytics: RespData
    analytics_columns: RespData
    analytics_dates: RespData


# securities listing
class SecuritiesListingParams(LangParams):
    date: Optional[str] = "today"
    start: Optional[str] = "0" # Показывать данные с N-й строки.
    # Данные отдаются блоками по 5000 строк.
    # Если дата не указана - отображаются наиболее актуальные данные
    
def new_securities_listing_params(
        lang: str = "ru",
        date: str = None,
        start: str = "0",
) -> SecuritiesListingParams:
    return SecuritiesListingParams(
        lang=lang,
        date=date,
        start=start,
    )
    
class SecuritiesListing(BaseModel):
    securities_listing: RespData
    securities_listing_updated: RespData
    securities_listing_dates: RespData


# aggregates
class AggregatesParams(LangParams):
    date: Optional[str] = "today"

def new_aggregates_params(
        lang: str = "ru",
        date: str = None,
) -> AggregatesParams:
    return AggregatesParams(
        lang=lang,
        date=date,
    )
    
class Aggregates(BaseModel):
    aggregates: RespData
    aggregates_dates: RespData


#aggregates columns
class AggregatesColumns(BaseModel):
    aggregates_columns: RespData


# analytics indices 
class AnalyticsIndicesParams(LangParams):
    security_collection: Optional[str]
    tradingsession: Optional[str]  # Показать данные только за необходимую сессию
    # 1 - Основная
    # 2 - Вечерняя
    # 3 - Итого (по умолчанию)

def new_analytics_indices_params(
        lang: str = "ru",
        security_collection: str = None,
        tradingsession: str = None,
) -> AnalyticsIndicesParams:
    return AnalyticsIndicesParams(
        lang=lang,
        security_collection=security_collection,
        tradingsession=tradingsession,
    )
    
class AnalyticsIndices(BaseModel):
    indices: RespData


# analytics index 
class AnalyticsIndexParams(LangParams):
    date: Optional[str] = "today"
    start: Optional[int] = 0
    tickers: Optional[str]
    tradingsession: Optional[str]  # Показать данные только за необходимую сессию
    # 1 - Основная
    # 2 - Вечерняя
    # 3 - Итого (по умолчанию)

def new_analytics_index_params(
        lang: str = "ru",
        date: str = "today", 
        start: int = 0,
        tickers: str = None,
        tradingsession: str = None,
) -> AnalyticsIndexParams:
    return AnalyticsIndexParams(
        lang=lang,
        date=date,
        start=start,
        tickers=tickers,
        tradingsession=tradingsession,
    )
    
class AnalyticsIndex(BaseModel):
    analytics: RespData
    analytics_cursor: RespData
    analytics_dates: RespData


# tickers
class AnalyticsTickersParams(BaseModel):
    date: Optional[str] = "today"
    tradingsession: Optional[str] = "3" # Показать данные только за необходимую сессию
    # 1 - Основная
    # 2 - Вечерняя
    # 3 - Итого (по умолчанию)

    def as_dict(self):
        return self.dict(exclude_none=True)
    
def new_analytics_tickers_params(
        date: str = "today", 
        tradingsession: str = "3",
) -> AnalyticsTickersParams:
    return AnalyticsTickersParams(
        date=date,
        tradingsession=tradingsession,
    )
    
class AnalyticsTickers(BaseModel):
    tickers: RespData


class AnalyticsTickerParams(LangParams):
    from_at: Optional[str] 
    till: Optional[str] = "1900-01-01"
    tradingsession: Optional[str] = "3" # Показать данные только за необходимую сессию
    # 1 - Основная
    # 2 - Вечерняя
    # 3 - Итого (по умолчанию)
    start: Optional[int] = 0

    def as_dict(self):
        params = self.dict(exclude_none=True)
        if params["from_at"]:
            params["from"] = params["from_at"]
            params.pop("from_at", None)

        return {k:v for k, v in params.items() if v is not None}
    
def new_analytics_ticker_params(
        from_at: str = None, 
        till: str = "1900-01-01",
        tradingsession: str = "3",
        start: int = 0,
) -> AnalyticsTickerParams:
    return AnalyticsTickerParams(
        from_at=from_at,
        till=till,
        tradingsession=tradingsession,
        start=start,
    )
    
class AnalyticsTicker(BaseModel):
    ticker: RespData
    ticker_cursor: RespData


# capitalization
class CapitalizationParams(LangParams):
    type: Optional[str] = "daily"
    date: Optional[str] = "today" 

    def as_dict(self):
        return self.dict(exclude_none=True)
    
def new_capitalization_params(
        type: str = "daily",
        date: str = "today",
) -> CapitalizationParams:
    return CapitalizationParams(
        type=type,
        date=date,
    )
    
class Capitalization(BaseModel):
    capitalization: RespData
    issue_capitalization : RespData

