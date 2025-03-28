# -*- coding: utf-8 -*-
"""
@File    : conftest.py
@Author  : zenhuawang
@Description : 
"""
import pytest

@pytest.fixture(scope="session")
def api_client():
    from utils.api_client import APIClient
    from config.config import load_config
    config = load_config()
    return APIClient(base_url=config['base_url'], headers=config['headers'])