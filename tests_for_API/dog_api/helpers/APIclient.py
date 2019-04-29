import json
import requests

class APIClient:
    HEADERS = {}

    def __init__(self, address):
        self.address = address

    def do_get(self, endpoint, verify_ssl=False, headers=HEADERS):
        url = "/".join([self.address, endpoint])
        return requests.get(url, headers=headers,
                            verify=verify_ssl)

    def do_post(self, endpoint, data=None, verify_ssl=False):
        url = "/".join([self.address, endpoint])
        headers = self.HEADERS
        headers["Content-type"] = "application/json"
        return requests.post(url, data, headers=headers, verify=verify_ssl)