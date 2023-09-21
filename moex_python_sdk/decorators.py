from time import time
from functools import wraps

from moex_python_sdk.models import new_resp_info


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


def responce(method):
    @wraps(method)
    def decorator(*args, **kwargs):
        """return model.Resp"""
        url, content = method(*args, **kwargs)

        return new_resp_info(url=url, content=content)

    return decorator

def resp(cls):
    class NewCls:
        def __init__(self, *args, **kwargs):
            self._obj = cls(*args, **kwargs)

        def __getattribute__(self, s):
            try:
                x = super().__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x

            attr = self._obj.__getattribute__(s)

            if isinstance(attr, type(self.__init__)):
                return responce(attr)
            else:
                return attr

    return NewCls

