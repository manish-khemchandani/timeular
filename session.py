import json
import requests
import urls

HEADERS = {
    'Content-Type': 'application/json'
}


class SessionManager(object):
    def __init__(self):
        self.session = requests.session()
        self.session.headers = HEADERS

    def login(self):
        payload = json.dumps({
            "apiKey": "redacted",
            "apiSecret": "redacted",
        })
        response = self.session.post(
            urls.SIGN_IN,
            data=payload,
        ).json()
        self.session.headers.update({"Authorization": "Bearer {}".format(response.get("token"))})
        return response

    def get(self, url, payload=None):
        if payload is None:
            payload = {}
        response = self.session.get(
            str(url),
            data=payload,
        )
        if response.status_code == 200:
            return response.json()
