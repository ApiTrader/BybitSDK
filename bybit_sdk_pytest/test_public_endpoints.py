import pytest
from bybit_sdk.bybit_client import ByBitClient

def test_server_time():
    client = ByBitClient()
    res = client.get_server_time()
    assert res.get('ret_code') == 0


