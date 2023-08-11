from time import time
from functools import wraps

import pandas as pd

from moex_python_sdk.models import Resp, RespData, new_resp_info


def time_it(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        start_time = time()
        func = f(*args, **kwargs)
        end_time = time()

        print("Func: %r took: %2.4f sec" % \
            (f.__name__, end_time - start_time))

        return func

    return decorator

# import pandas as pd

# my_dict = {'Computer':1500,'Monitor':300,'Printer':150,'Desk':250}
# df = pd.DataFrame(list(my_dict.items()),columns = ['Products','Prices'])

# print (df)
# print (type(df))

def resp(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        """return model.Resp"""
        url, content = f(*args, **kwargs)

        return new_resp_info(url=url, content=content)
    
    return decorator



def return_df(f) -> pd.DataFrame:
    @wraps(f)
    def decorator(*args, **kwargs):
        data = f(*args, **kwargs)
        df = pd.DataFrame(data["data"], columns=data["columns"])

        return df

    return decorator

