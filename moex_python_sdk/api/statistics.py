from moex_python_sdk.api._api import BaseApi
from moex_python_sdk.decorators import resp

from moex_python_sdk.models import LangParams, new_resp_data
from moex_python_sdk.models.securities import Securities
from moex_python_sdk.models.statistics import (
    StatisticRates,
    StatisticRatesColumns,
    StatisticDerivativesReportParams,
    StatisticDerivativesReport,
    StatisticFixingParams,
    StatisticFixing,
    IndicativeratesSecuritiesParams,
    IndicativeratesSecurities,
    IndicativeratesSecurityParams,
    IndicativeratesSecurity,
    MarketsFixingParams,
    MarketsFixing,
    StatisticMarketParams,
    MarketsSecurityParams,
    StatisticsAssetsParams,
    StatisticsAssets,
    StatisticsAsset,
    AssetOptionboardParams,
    AssetOptionboar,
    AssetOpenpositionsParams,
    AssetOpenpositions,
    AssetTurnoversParams,
    AssetTurnovers,
    ComplexSecuritiesParams,
    ComplexSecurity,
    SharesCorrelationsParams,
    SharesCorrelations,
    CbrfParams,
    Cbrf,
    Splits,
    MirpParams,
    Mirp,
    DealersParams,
    Dealers,
    CboperParams,
    Cboper,
    DeviationcoeffsParams,
    Deviationcoeffs,
    QuotedSecuritiesParams,
    QuotedSecurities,
    CurrentPricesParams,
    CurrentPrices,
    MonthendaccintsParams,
    Monthendaccints,
    AnalyticsColumns,
    BulletinsParams,
    Bulletins,
    RusfarParams,
    Rusfar,
    SecuritiesListingParams,
    SecuritiesListing,
    AggregatesParams,
    Aggregates,
    AggregatesColumns,
    AnalyticsIndicesParams,
    AnalyticsIndices,
    AnalyticsIndexParams,
    AnalyticsIndex,
    AnalyticsTickersParams,
    AnalyticsTickers,
    AnalyticsTickerParams,
    AnalyticsTicker,
    CapitalizationParams,
    Capitalization,
)


@resp
class StatisticApi:
    def __init__(self, api: BaseApi):
        """Только для авторизированных подписчиков биржи"""
        self.api = api
        self.endpoint = "/statistics"

    def get_complex_securities(self, params: ComplexSecuritiesParams, format: str = "json"):
        """Маркировка сложных финансовых инструментов."""

        r = self.api.get(
            f"{self.endpoint}/complex/securities.{format}",
            params=params.as_dict(),
        )
        
        return r["url"], Securities(securities=new_resp_data(r["data"]["securities"]))

    def get_complex_security(self, security: str, format: str = "json"):
        """Маркировка сложных финансовых инструментов - Инструмент."""

        r = self.api.get(
            f"{self.endpoint}/complex/securities/{security}.{format}",
        )

        return r["url"], ComplexSecurity(
            securities=new_resp_data(r["data"]["securities"]),
            security_columns=new_resp_data(r["data"]["security.columns"]),
        )

    def get_market(self, engine: str, market: str, params: LangParams, format: str = "json"):
        """Курсы переоценки коллатеральных инструментов."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}.{format}",
            params=params.as_dict(),
        )

        return r["url"], Securities(securities=new_resp_data(r["data"]["securities"]))

    def get_market_securities(self, engine: str, market: str, params: StatisticMarketParams, format: str = "json"):
        """Курсы переоценки коллатеральных инструментов."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/securities.{format}",
            params=params.as_dict(),
        )

        return r["url"], Securities(securities=new_resp_data(r["data"]["securities"]))

    def get_market_security(self, engine: str, market: str, security: str, params: MarketsSecurityParams, format: str = "json"):
        """Курсы переоценки коллатеральных инструментов."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/markets/{market}/securities/{security}.{format}",
            params=params.as_dict(check=True),
        )

        return r["url"], Securities(securities=new_resp_data(r["data"]["securities"]))

    def get_derivatives_report(self, engine: str, report_name: str, params: StatisticDerivativesReportParams, format: str = "json"):
        """Еженедельные отчеты по валютным деривативам:
        * numtrades - Информация о количестве договоров по инструментам, являющимся производными финансовыми инструментами (по валютным парам)
        * participants - Информация о количестве лиц, имеющих открытые позиции по инструментам, являющимся производными финансовыми инструментами (по валютным парам)
        * openpositions - Информация об открытых позициях по инструментам, являющимся производными финансовыми инструментами (по валютным парам)
        * expirationparticipants - Информация о количестве лиц, имеющих открытые позиции по договорам, являющимся производными финансовыми инструментами (по срокам экспирации)
        * expirationopenpositions - Информация об объеме открытых позиций по договорам, являющимся производными финансовыми инструментами (по срокам экспирации)."""

        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/derivatives/{report_name}.{format}",
            params=params.as_dict(),
        )

        return r["url"], StatisticDerivativesReport(
            columns=new_resp_data(r["data"]["columns"]),
            data=new_resp_data(r["data"]["data"]),
        )

    def get_monthly_report(self, engine: str, report_name: str, params:  StatisticDerivativesReportParams, format: str = "json"):
        r = self.api.get(
            f"{self.endpoint}/engines/{engine}/monthly/{report_name}.{format}",
            params=params.as_dict(),
        )

        return r["url"], StatisticRatesColumns(columns=new_resp_data(r["data"]["columns"]))

    def get_fixing(self, params: MarketsFixingParams, format: str = "json"):
        """Фиксинги Московской биржи."""

        r = self.api.get(
            f"{self.endpoint}/engines/currency/markets/fixing.{format}",
            params=params.as_dict(),
        )

        return r["url"], MarketsFixing(
            history=new_resp_data(r["data"]["history"]),
            history_dates=new_resp_data(r["data"]["history.dates"]),
        )

    def get_fixing_security(self, security: str, params: StatisticFixingParams, format: str = "json"):
        """Фиксинги Московской биржи."""

        r = self.api.get(
            f"{self.endpoint}/engines/currency/markets/fixing/{security}.{format}",
            params=params.as_dict(check=True),
        )

        return r["url"], StatisticFixing(
            history=new_resp_data(r["data"][""]),
            history_cursor=new_resp_data(r["data"]["history.cursor"]),
            history_dates=new_resp_data(r["data"]["history.dates"]),
        )

    def get_selt_rates(self, params: CbrfParams, format: str = "json"):
        """Курсы ЦБРФ."""

        r = self.api.get(
            f"{self.endpoint}/engines/currency/markets/selt/rates.{format}",
            params=params.as_dict(),
        )

        return r["url"], Cbrf(
            cbrf=new_resp_data(r["data"]["cbrf"]),
            wap_rates=new_resp_data(r["data"]["wap_rates"]),
        )

    def get_indicativerates_securities(self, params: IndicativeratesSecuritiesParams, format: str = "json"):
        """Индикативные курсы валют срочного рынка."""

        r = self.api.get(
            f"{self.endpoint}/engines/futures/markets/indicativerates/securities.{format}",
            params=params.as_dict(),
        )

        return r["url"], IndicativeratesSecurities(
            securities=new_resp_data(r["data"]["securities"]),
            securities_list=new_resp_data(r["data"]["securities.list"]),
        )

    def get_indicativerates_security(self, security: str, params: IndicativeratesSecurityParams, format: str = "json"):
        """Индикативный курс валют срочного рынка."""

        r = self.api.get(
            f"{self.endpoint}/engines/futures/markets/indicativerates/securities/{security}.{format}",
            params=params.as_dict(check=True),
        )

        return r["url"], IndicativeratesSecurity(
            security=new_resp_data(r["data"]["security"]),
            securities_cursor=new_resp_data(r["data"]["securities.cursor"]),
            securities_dates=new_resp_data(r["data"]["securities.dates"]),
            securities_current=new_resp_data(r["data"]["securities.current"]),
        )

    def get_options_assets(self, params: StatisticsAssetsParams, format: str = "json"):
        """Опционные серии."""

        r = self.api.get(
            f"{self.endpoint}/engines/futures/markets/options/assets.{format}",
            params=params.as_dict(),
        )

        return r["url"], StatisticsAssets(asset_volumes=new_resp_data(r["data"]["asset_volumes"]))

    def get_options_asset(self, asset: str, format: str = "json"):
        """Опционные серии."""

        r = self.api.get(
            f"{self.endpoint}/engines/futures/markets/options/assets/{asset}.{format}",
        )

        return r["url"], StatisticsAsset(expirations=new_resp_data(r["data"]["expirations"]))


    def get_openpositions(self, asset: str, params: AssetOpenpositionsParams, format: str = "json"):
        """Открытые позиции по опционной серии."""

        r = self.api.get(
            f"{self.endpoint}/engines/futures/markets/options/assets/{asset}/openpositions.{format}",
            params=params.as_dict(),
        )

        return r["url"], AssetOpenpositions(open_positions=new_resp_data(r["data"]["open_positions"]))

    def get_optionboard(self, asset: str, params: AssetOptionboardParams, format: str = "json"):
        """Доска опционов"""

        r = self.api.get(
            f"{self.endpoint}/engines/futures/markets/options/assets/{asset}/optionboard.{format}",
            params=params.as_dict(),
        )

        return r["url"], AssetOptionboar(
            call=new_resp_data(r["data"]["call"]),
            put=new_resp_data(r["data"]["put"]),
            asset=new_resp_data(r["data"]["asset"]),
        )

    def get_volumes_options_asset(self, asset: str, params: StatisticMarketParams, format: str = "json"):
        """Объем торгов для опционной серии."""

        r = self.api.get(
            f"{self.endpoint}/engines/futures/markets/options/assets/{asset}/volumes.{format}",
            params=params.as_dict(),
        )

        return r["url"], StatisticsAssets(asset_volumes=new_resp_data(r["data"]["asset_volumes"]))

    def get_turnovers(self, asset: str, params: AssetTurnoversParams, format: str = "json"):
        """Объем торгов для опционной серии."""

        r = self.api.get(
            f"{self.endpoint}/engines/futures/markets/options/assets/{asset}/turnovers.{format}",
            params=params.as_dict(),
        )

        return r["url"], AssetTurnovers(asset_turnovers=new_resp_data(r["data"]["asset_turnovers"]))

    def get_repo_mirp(self, params: MirpParams, format: str = "json"):
        r = self.api.get(
            f"{self.endpoint}/engines/state/markets/repo/mirp.{format}",
            params=params.as_dict(),
        )

        return r["url"], Mirp(
            data=new_resp_data(r["data"]["data"]),
            data_cursor=new_resp_data(r["data"]["data.cursor"]),
            data_dates=new_resp_data(r["data"]["data.dates"]),
        )

    def get_repo_dealers(self, params: DealersParams, format: str = "json"):
        r = self.api.get(
            f"{self.endpoint}/engines/state/markets/repo/dealers.{format}",
            params=params.as_dict(),
        )

        return r["url"], Dealers(
            data=new_resp_data(r["data"]["data"]),
            data_dates=new_resp_data(r["data"]["data.dates"]),
        )

    def get_repo_cboper(self, params: CboperParams, format: str = "json"):
        """Средневзвешенные ставки по операциям центрального банка."""

        r = self.api.get(
            f"{self.endpoint}/engines/state/markets/repo/cboper.{format}",
            params=params.as_dict(),
        )

        return r["url"], Cboper(
            date=new_resp_data(r["data"]["data"]),
            dates=new_resp_data(r["data"]["dates"]),
        )

    def get_state_rates(self, params: LangParams, format: str = "json"):
        r = self.api.get(
            f"{self.endpoint}/engines/state/rates.{format}",
            params=params.as_dict(),
        )

        return r["url"], StatisticRates(
            auctions=new_resp_data(r["data"]["auctions"]),
            fixed=new_resp_data(r["data"]["fixed"]),
        )


    def get_state_rates_columns(self, params: LangParams, format: str = "json"):
        r = self.api.get(
            f"{self.endpoint}/engines/state/rates/columns.{format}",
            params=params.as_dict(),
        )

        return r["url"], StatisticRatesColumns(columns=new_resp_data(r["data"]["columns"]))

    def get_stock_capitalization(self, params: CapitalizationParams, format: str = "json"):
        """Капитализация фондового рынка."""

        r = self.api.get(
            f"{self.endpoint}/engines/stock/capitalization.{format}",
            params=params.as_dict(),
        )

        return r["url"], Capitalization(
            capitalization=new_resp_data(r["data"]["capitalization"]),
            issue_capitalization=new_resp_data(r["data"]["issuecapitalization"]),
        )

    def get_stock_current_prices(self, params: CurrentPricesParams, format: str = "json"):
        """Текущие цены бумаг."""

        r = self.api.get(
            f"{self.endpoint}/engines/stock/currentprices.{format}",
            params=params.as_dict(),
        )

        return r["url"], CurrentPrices(
            currentprices=new_resp_data(r["data"]["currentprices"]),
            currentprices_dates=new_resp_data(r["data"]["currentprices.dates"]),
        )

    def get_stock_deviation_coeffs(self, params: DeviationcoeffsParams, format: str = "json"):
        """Показатели для определения критериев существенного отклонения."""

        r = self.api.get(
            f"{self.endpoint}/engines/stock/deviationcoeffs.{format}",
            params=params.as_dict(),
        )

        return r["url"], Deviationcoeffs(
            securities=new_resp_data(r["data"]["securities"]),
            securities_cursor=new_resp_data(r["data"]["securities.cursor"]),
            securities_dates=new_resp_data(r["data"]["securities.dates"]),
        )

    def get_stock_quoted_securities(self, params: QuotedSecuritiesParams, format: str = "json"):
        """Cписок акций, по которым рассчитывается рыночная котировка."""

        r = self.api.get(
            f"{self.endpoint}/engines/stock/quotedsecurities.{format}",
            params=params.as_dict(),
        )

        return r["url"], QuotedSecurities(
            quotedsecurities=new_resp_data(r["data"]["securities"]),
            quotedsecurities_dates=new_resp_data(r["data"]["quotedsecurities.dates"]),
        )

    def get_bonds_aggregates(self, params: AggregatesParams, format: str = "json"):
        """Агрегированные показатели рынка облигаций."""

        r = self.api.get(
            f"{self.endpoint}/engines/stock/markets/bonds/aggregates.{format}",
            params=params.as_dict(),
        )

        return r["url"], Aggregates(
            aggregates=new_resp_data(r["data"]["securities"]),
            aggregates_dates=new_resp_data(r["data"]["aggregates.dates"]),
        )

    def get_bonds_aggregates_column(self, params: LangParams, format: str = "json"):
        r = self.api.get(
            f"{self.endpoint}/engines/stock/markets/bonds/aggregates/columns.{format}",
            params=params.as_dict(),
        )

        return r["url"], AggregatesColumns(aggregates_columns=new_resp_data(r["data"]["aggregates.columns"]))

    def get_bonds_month_end_accints(self, params: MonthendaccintsParams, format: str = "json"):
        """НКД на конец месяца."""

        r = self.api.get(
            f"{self.endpoint}/engines/stock/markets/bonds/monthendaccints.{format}",
            params=params.as_dict(),
        )

        return r["url"], Monthendaccints(
            monthend_accints=new_resp_data(r["data"]["monthend_accints"]),
            monthend_accints_index=new_resp_data(r["data"]["monthend_accints.index"]),
        )

    def get_index_analytics(self, params: AnalyticsIndicesParams, format: str = "json"):
        """Индексы фондового рынка."""

        r = self.api.get(
            f"{self.endpoint}/engines/stock/markets/index/analytics.{format}",
            params=params.as_dict(),
        )

        return r["url"], AnalyticsIndices(indices=new_resp_data(r["data"]["indices"]))

    def get_analytics_columns(self, params: LangParams, format: str = "json"):
        r = self.api.get(
            f"{self.endpoint}/engines/stock/markets/index/analytics/columns.{format}",
            params=params.as_dict(),
        )

        return r["url"], AnalyticsColumns(analytics_columns=new_resp_data(r["data"]["analytics.columns"]))

    def get_analytics_by_index(self, index_id: str, params: AnalyticsIndexParams, format: str = "json"):
        """Аналитические показатели за дату."""

        r = self.api.get(
            f"{self.endpoint}/engines/stock/markets/index/analytics/{index_id}.{format}",
            params=params.as_dict(),
        )

        return r["url"], AnalyticsIndex(
            analytics=new_resp_data(r["data"]["analytics"]),
            analytics_cursor=new_resp_data(r["data"]["analytics.cursor"]),
            analytics_dates=new_resp_data(r["data"]["analytics.dates"]),
        )

    def get_tickers(self, index_id: str, params: AnalyticsTickersParams, format: str = "json"):
        """Список тикеров за все время торгов."""

        r = self.api.get(
            f"{self.endpoint}/engines/stock/markets/index/analytics/{index_id}/tickers.{format}",
            params=params.as_dict(),
        )

        return r["url"], AnalyticsTickers(tickers=new_resp_data(r["data"]["tickers"]))

    def get_ticker(self, index_id: str, ticker: str, params: AnalyticsTickerParams, format: str = "json"):
        """Информация по тикеру."""

        r = self.api.get(
            f"{self.endpoint}/engines/stock/markets/index/analytics/{index_id}/tickers/{ticker}.{format}",
            params=params.as_dict(check=True),
        )

        return r["url"], AnalyticsTicker(
            ticker=new_resp_data(r["data"]["ticker"]),
            ticker_cursor=new_resp_data(r["data"]["ticker.cursor"]),
        )

    def get_index_bulletins(self, params: BulletinsParams, format: str = "json"):
        """Бюллетени для индексов."""

        r = self.api.get(
            f"{self.endpoint}/engines/stock/markets/index/bulletins.{format}",
            params=params.as_dict(),
        )

        return r["url"], Bulletins(bulletins=new_resp_data(r["data"]["bulletins"]))

    def get_index_rusfar(self, params: RusfarParams, format: str = "json"):
        """RUSFAR расшифровка показателей."""

        r = self.api.get(
            f"{self.endpoint}/engines/stock/markets/index/rusfar.{format}",
            params=params.as_dict(),
        )

        return r["url"], Rusfar(
            analytics=new_resp_data(r["data"]["analytics"]),
            analytics_columns=new_resp_data(r["data"]["analytics.columns"]),
            analytics_dates=new_resp_data(r["data"]["analytics.dates"]),
        )

    def get_shares_correlations(self, params: SharesCorrelationsParams, format: str = "json"):
        """Коэффициенты корелляции фондового рынка."""

        r = self.api.get(
            f"{self.endpoint}/engines/stock/markets/shares/correlations.{format}",
            params=params.as_dict(),
        )

        return r["url"], SharesCorrelations(
            coefficients=new_resp_data(r["data"]["coefficients"]),
            coefficients_cursor=new_resp_data(r["data"]["coefficients.cursor"]),
            coefficients_dates=new_resp_data(r["data"]["coefficients.dates"]),
        )

    def get_stock_securities_listing(self, params: SecuritiesListingParams, format: str = "json"):
        """Таблица соответствия торгуемых ценных бумаг по режимам торгов."""

        r = self.api.get(
            f"{self.endpoint}/engines/stock/securitieslisting.{format}",
            params=params.as_dict(),
        )

        return r["url"], SecuritiesListing(
            securities_listing=new_resp_data(r["data"]["securitieslisting"]),
            securities_listing_updated=new_resp_data(r["data"]["securitieslisting.updated"]),
            securities_listing_columns=new_resp_data(r["data"]["securitieslisting.columns"]),
            securities_listing_dates=new_resp_data(r["data"]["securitieslisting.dates"]),
        )

    def get_stock_splits(self, format: str = "json"):
        """Справочник дроблений и консолидаций бумаг фондового рынка."""

        r = self.api.get(
            f"{self.endpoint}/engines/stock/splits.{format}",
        )

        return r["url"], Splits(splits=new_resp_data(r["data"]["splits"]))

    def get_splits_security(self, security: str, format: str = "json"):
        r = self.api.get(
            f"{self.endpoint}/engines/stock/splits/{security}.{format}",
        )

        return r["url"], Splits(splits=new_resp_data(r["data"]["splits"]))

