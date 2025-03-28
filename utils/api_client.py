# -*- coding: utf-8 -*-
"""
@File    : api_client.py
@Author  : zenhuawang
@Description : 
"""
import requests

class APIClient:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers

    def request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, headers=self.headers, **kwargs)
        return response