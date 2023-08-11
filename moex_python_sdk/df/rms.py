from moex_python_sdk.api import MoexApi
from moex_python_sdk.decorators import return_df


class Rms:
    def __init__(self, api: MoexApi):
        self.api = api.rms()


    @return_df
    def get_rms_object(self, engine: str, object: str):        
        return self.api.get_rms_object(engine, object)
    
    ########## TODO ##################################################################
    @return_df
    def get_rms_object_1(self, engine: str, object: str):
        return self.api.get_rms_object(engine, object)
    
    @return_df
    def get_rms_object_2(self, engine: str, object: str):
        return self.api.get_rms_object(engine, object)
    
    @return_df
    def get_rms_object_3(self, engine: str, object: str):
        return self.api.get_rms_object(engine, object)
    ##########################################################################################################3


    @return_df
    def get_irr(self, engine: str):
        return self.api.get_irr(engine)
    
    @return_df
    def get_irr_filters(self, engine: str):
        return self.api.get_irr_filters(engine)
    
    @return_df
    def get_settlements_calendar(self, engine: str):
        return self.api.get_settlements_calendar(engine)