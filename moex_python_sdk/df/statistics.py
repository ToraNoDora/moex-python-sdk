from moex_python_sdk.api import MoexApi
from moex_python_sdk.decorators import return_df


class Statistic:
    def __init__(self, api: MoexApi):
        self.api = api.statistic()


    @return_df
    def get_complex_securities(self):
        return self.api.get_complex_securities()
    
    @return_df
    def get_complex_security(self, security: str):
        return self.api.get_complex_security(security)
    
    @return_df
    def get_market(self, engine: str, market: str):
        return self.api.get_market(engine, market)
    
    @return_df
    def get_market_securities(self, engine: str, market: str):
        return self.api.get_market_securities(engine, market)
    
    @return_df
    def get_market_security(self, engine: str, market: str, security: str):
        return self.api.get_market_security(engine, market, security)
    
    @return_df
    def get_derivatives_report(self, engine: str, report_name: str):
        return self.api.get_derivatives_report(engine, report_name)
    
    @return_df
    def get_monthly_report(self, engine: str, report_name: str):
        return self.api.get_monthly_report(engine, report_name)
    
    @return_df
    def get_fixing(self):
        return self.api.get_fixing()
    
    @return_df
    def get_fixing_security(self, security: str):
        return self.api.get_fixing_security(security)
    
    @return_df
    def get_selt_rates(self):
        return self.api.get_selt_rates()
    
    @return_df
    def get_indicativerates_securities(self):
        return self.api.get_indicativerates_securities()
    
    @return_df
    def get_indicativerates_securities(self, security: str):
        return self.api.get_indicativerates_securities(security)
    
    @return_df
    def get_options_assets(self):
        return self.api.get_options_assets()
    
    @return_df
    def get_options_asset(self, asset: str):
        return self.api.get_options_asset(asset)
    
    @return_df
    def get_openpositions(self, asset: str):
        return self.api.get_openpositions(asset)
    
    @return_df
    def get_optionboard(self, asset: str):
        return self.api.get_optionboard(asset)
    
    @return_df
    def get_volumes_options_asset(self, asset: str):
        return self.api.get_volumes_options_asset(asset)
    
    @return_df
    def get_turnovers(self, asset: str):
        return self.api.get_turnovers(asset)
    
    @return_df
    def get_repo_mirp(self):
        return self.api.get_repo_mirp()
    
    @return_df
    def get_repo_dealers(self):
        return self.api.get_repo_dealers()
    
    @return_df
    def get_repo_cboper(self):
        return self.api.get_repo_cboper()
    
    @return_df
    def get_state_rates(self):
        return self.api.get_state_rates()
    
    @return_df
    def get_state_rates_columns(self):
        return self.api.get_state_rates_columns()

    @return_df
    def get_stock_capitalization(self):
        return self.api.get_stock_capitalization()
    
    @return_df
    def get_stock_current_prices(self):
        return self.api.get_stock_current_prices()
    
    @return_df
    def get_stock_deviation_coeffs(self):
        return self.api.get_stock_deviation_coeffs()
    
    @return_df
    def get_stock_quoted_securities(self):
        return self.api.get_stock_quoted_securities()
    
    @return_df
    def get_bonds_aggregates(self):
        return self.api.get_bonds_aggregates()
    
    @return_df
    def get_bonds_aggregates_column(self):
        return self.api.get_bonds_aggregates_column()
    
    @return_df
    def get_bonds_month_end_accints(self):
        return self.api.get_bonds_month_end_accints()
    
    @return_df
    def get_index_analytics(self):
        return self.api.get_index_analytics()
    
    @return_df
    def get_analytics_columns(self):
        return self.api.get_analytics_columns()
    
    @return_df
    def get_analytics_by_index(self, index_id: str):
        return self.api.get_analytics_by_index(index_id)
    
    @return_df
    def get_tickers(self, index_id: str):
        return self.api.get_tickers(index_id)
    
    @return_df
    def get_tickers(self, index_id: str, ticker: str):
        return self.api.get_tickers(index_id, ticker)
    
    @return_df
    def get_index_bulletins(self):
        return self.api.get_index_bulletins()
    
    @return_df
    def get_index_rusfar(self):
        return self.api.get_index_rusfar()
    
    @return_df
    def get_shares_correlations(self):
        return self.api.get_shares_correlations()
    
    @return_df
    def get_stock_securities_listing(self):
        return self.api.get_stock_securities_listing()
    
    @return_df
    def get_stock_splits(self):
        return self.api.get_stock_splits()
    
    @return_df
    def get_splits_security(self, security: str):
        return self.api.get_splits_security(security)
