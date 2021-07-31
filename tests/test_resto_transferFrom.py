import pytest
import logging
from brownie import Wei, reverts
LOGGER = logging.getLogger(__name__)


def test_restonxt20_transferFrom(accounts, restonxt20):
    restonxt20.transfer(accounts[1], 1, {"from": accounts[0]})
    with reverts("ERC20: transfer amount exceeds allowance"):
        restonxt20.transferFrom(accounts[1], accounts[2], 1, {"from": accounts[2]})
    restonxt20.approve(accounts[0], 1, {"from": accounts[1]})    
    restonxt20.transferFrom(accounts[1], accounts[2], 1, {"from": accounts[0]})
    assert restonxt20.balanceOf(accounts[1]) == 0
    assert restonxt20.balanceOf(accounts[2]) == 1

    #minter
    restonxt20.transfer(accounts[1], 1, {"from": accounts[0]})
    restonxt20.approve(accounts[2], 1, {"from": accounts[1]})
    restonxt20.transferFrom(accounts[1], accounts[2], 1, {"from": accounts[2]})
    assert restonxt20.balanceOf(accounts[1]) == 0
    assert restonxt20.balanceOf(accounts[2]) == 2

    restonxt20.approve(accounts[3], 1, {"from": accounts[1]})
    with reverts("ERC20: transfer amount exceeds balance"):
        restonxt20.transferFrom(accounts[1], accounts[3], 1, {"from": accounts[3]})

def test_increaseAllowance(accounts, restonxt20):
    before = restonxt20.allowance(accounts[1], accounts[3])
    tx = restonxt20.increaseAllowance(accounts[3], 1e18, {'from': accounts[1]})
    assert len(tx.events['Approval']) == 1
    assert before == restonxt20.allowance(accounts[1], accounts[3]) - 1e18       


def test_decreaseAllowance(accounts, restonxt20):
    before = restonxt20.allowance(accounts[1], accounts[3])
    tx = restonxt20.decreaseAllowance(accounts[3], 1e18, {'from': accounts[1]})
    assert len(tx.events['Approval']) == 1
    assert before == restonxt20.allowance(accounts[1], accounts[3]) + 1e18       

def test_decreaseAllowance_fail(accounts, restonxt20):
    with reverts("ERC20: decreased allowance below zero"):
        restonxt20.decreaseAllowance(accounts[4], 1e18, {'from': accounts[0]})
