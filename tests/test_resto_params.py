import pytest
import logging
from brownie import Wei, reverts
LOGGER = logging.getLogger(__name__)


def test_restonxt_params(accounts, restonxt20):
    assert restonxt20.totalSupply() == restonxt20.MAX_SUPPLY()
    assert restonxt20.symbol() == 'RESTO'
    assert restonxt20.name() == 'Resto Token'
    assert restonxt20.decimals() == 18



