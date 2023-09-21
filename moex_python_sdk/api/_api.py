from typing import Optional
from requests import Response, Session


class BaseApi:
    """Утилитарный класс, который предоставляет обертку над API"""

    def __init__(self, base_url: str, session: Session, verify: Optional[str] = False, warnings: bool = True):
        if not warnings:
            import requests
            requests.packages.urllib3.disable_warnings()

        self.url = base_url
        self.session = session
        self.session.verify = verify
        self.access_token = None

    def update_access_token(self, new_token):
        self.access_token = new_token
        self.session.headers.update({"Authorization": "Bearer " + new_token})

    def get(self, url: str, params=None, **kwargs):
        r = self.session.get(self.url + url, params=params)

        return self.parse_response(r, **kwargs)

    def post(self, url, params=None, json=None, headers=None, override_get=False, **kwargs):
        if headers is None:
            headers = {}
        if override_get:
            headers["X-HTTP-Method-Override"] = "GET"

        r = self.session.post(self.url + url, headers=headers, params=params, json=json)
        return self.parse_response(r, **kwargs)

    def parse_response(self, response: Response, **kwargs):
        as_json = kwargs.get("as_json", True)
        if as_json:
            return {
                "url": response.url,
                "status": response.status_code,
                "data": response.json(),
            }

        return response

