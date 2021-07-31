import pytest

@pytest.fixture(scope="module")
def restonxt20(accounts, RestoNXT):
    erc20 = accounts[0].deploy(RestoNXT, accounts[0])
    yield erc20 


 



