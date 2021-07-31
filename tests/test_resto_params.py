import pytest
import logging
from brownie import Wei, reverts
LOGGER = logging.getLogger(__name__)


def test_restonxt_params(accounts, restonxt20):
    assert restonxt20.totalSupply() == restonxt20.MAX_SUPPLY()
    assert restonxt20.symbol() == 'RESTO'
    assert restonxt20.name() == 'Resto Token'

def test_restonxt_transfer(accounts, restonxt20):
    before_balance = restonxt20.balanceOf(accounts[0])
    logging.info('acc = {}'.format(restonxt20.balanceOf(accounts[0])))
    restonxt20.transfer(accounts[0], 1e18, {"from":accounts[0]})
    assert restonxt20.balanceOf(accounts[0]) == before_balance


