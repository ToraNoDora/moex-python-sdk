from requests import Response, Session


class BaseApi:
    """Утилитарный класс, который предоставляет обертку над API"""

    def __init__(self, base_url: str, session: Session, verify: bool = False, warnings: bool = False): # TODO warnings = True
        self.url = base_url
        if not warnings:
            import requests
            requests.packages.urllib3.disable_warnings() # warning, that needing ssl certeficates

        self.session = session
        self.session.verify = verify # ssl certificates

    def get(self, url: str, params=None, **kwargs):
        r = self.session.get(self.url + url, params=params)
        
        return self.parse_response(r, **kwargs)

    def parse_response(self, response: Response, **kwargs):
        as_json = kwargs.get("as_json", True)

        if as_json:
            return response.json()

        return response

