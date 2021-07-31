// SPDX-License-Identifier: MIT

// RestoNXT project token ERC20

//***************************************************************
// ERC20 part of this contract based on best community practice 
// of https://github.com/OpenZeppelin/zeppelin-solidity
// Adapted and amended by IBERGroup, email:maxsizmobile@iber.group; 
// Code released under the MIT License.
////**************************************************************

pragma solidity ^0.8.6;

import "./ERC20.sol";

contract RestoNXT is ERC20 {

    uint256 constant public MAX_SUPPLY = 100_000_000e18;

    constructor(address initialKeeper)
    ERC20("Resto Token", "RESTO")
    { 
        //Initial supply mint  - review before PROD
        _mint(initialKeeper, MAX_SUPPLY);
    }
}

