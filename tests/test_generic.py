# -*- coding: utf-8 -*-
"""
@File    : test_generic.py
@Author  : zenhuawang
@Description : 
"""
import pytest
import yaml
from pathlib import Path
from utils.api_client import APIClient


def load_test_cases():
    test_cases = []
    test_case_dir = Path(__file__).parent.parent / "test_cases"
    for yaml_file in test_case_dir.glob("*.yaml"):
        with open(yaml_file, 'r') as file:
            test_case = yaml.safe_load(file)
            # 使用文件名作为用例标识
            case_name = yaml_file.stem
            test_cases.append(pytest.param(test_case, id=case_name))
    return test_cases


@pytest.fixture
def api_client():
    from utils.api_client import APIClient
    from config.config import load_config
    config = load_config()
    return APIClient(base_url=config['base_url'], headers=config['headers'])


@pytest.mark.parametrize("test_case", load_test_cases(), ids=lambda x: x.id)
def test_generic(api_client, test_case):
    method = test_case['method']
    endpoint = test_case['endpoint']
    request_data = test_case.get('request', {})
    expected = test_case['expected']

    response = api_client.request(method, endpoint, **request_data)

    # 断言状态码
    assert response.status_code == expected['status_code']

    # 断言响应体（如果存在）
    if 'response' in expected:
        response_json = response.json()
        if isinstance(expected['response'], list):
            for expected_item in expected['response']:
                assert expected_item in response_json
        else:
            for key, value in expected['response'].items():
                assert response_json[key] == value