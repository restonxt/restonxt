## Restonxt project token


### Tests
We use Brownie framework for developing and unit test. For run tests
first please [install it](https://eth-brownie.readthedocs.io/en/stable/install.html)

```bash
brownie test
```
Don't forget [ganache-cli](https://www.npmjs.com/package/ganache-cli)

### Deployments Info
Deploy is very simple. You can find workflow in 
[fixtures](./tests/fixtures/deploy_env.py) 


#### 2021-08-03 Ethereum Mainnet
https://etherscan.io/address/0x45e756bd263ab8bf591f28f6286325e76479926a#code

#### 2021-07-31 Testnet Rinkeby
https://rinkeby.etherscan.io/address/0x13Ba5d5Eb87a198D14A0d5e245D388b814C1015c#code

---
#### Gas Consumption Info
```json
RestoNXT <Contract>
   ├─ constructor       -  avg: 641948  avg (confirmed): 641948  low: 641948  high: 641948
   ├─ approve           -  avg:  38541  avg (confirmed):  44087  low:  21905  high:  44091
   ├─ transfer          -  avg:  37925  avg (confirmed):  43245  low:  21970  high:  51025
   ├─ transferFrom      -  avg:  32029  avg (confirmed):  26026  low:  22276  high:  52491
   ├─ increaseAllowance -  avg:  30166  avg (confirmed):  30166  low:  30166  high:  30166
   └─ decreaseAllowance -  avg:  26662  avg (confirmed):  30186  low:  23139  high:  30186

```

#### Test Coverage Info
```python
contract: RestoNXT - 92.9%
    ERC20.allowance - 100.0%
    ERC20.approve - 100.0%
    ERC20.balanceOf - 100.0%
    ERC20.decimals - 100.0%
    ERC20.decreaseAllowance - 100.0%
    ERC20.increaseAllowance - 100.0%
    ERC20.name - 100.0%
    ERC20.symbol - 100.0%
    ERC20.totalSupply - 100.0%
    ERC20.transfer - 100.0%
    ERC20.transferFrom - 100.0%
    ERC20._transfer - 91.7%
    ERC20._approve - 87.5%


```

----


