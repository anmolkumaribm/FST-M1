import pytest

@pytest.fixture
def num_list():
    int_list = list(range(11))
    return int_list

@pytest.fixture
def wallet_amount():
   amount = 0
   return amount