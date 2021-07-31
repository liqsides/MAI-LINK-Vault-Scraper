from web3 import Web3
import sqlite3
from random import choice



url = ['wss://matic-mainnet-full-ws.bwarelabs.com', 'wss://rpc-mainnet.matic.quiknode.pro']
#url =  'wss://ws-matic-mainnet.chainstacklabs.com'

provider = Web3.WebsocketProvider(choice(url))

w3 = Web3(provider)
mai_address = '0xa3Fa99A148fA48D14Ed51d610c367C61876997F1'
liquidator_address = '0x61167073E31b1DAd85a3E531211c7B8F1E5cAE72'

file = 'C://Users/example/Desktop/link_db.db'
create_table = """ CREATE TABLE IF NOT EXISTS mai_link_vaults (
                            id int PRIMARY KEY,
                            collateral float,
                            debt float );"""
create = """ REPLACE INTO mai_link_vaults (
                    id,
                    collateral,
                    debt )
                    VALUES (?,?,?);"""

liquidator = w3.eth.contract(address=liquidator_address,
                             abi='[{"inputs":[{"internalType":"address","name":"ethPriceSourceAddress","type":"address"},{"internalType":"uint256","name":"minimumCollateralPercentage","type":"uint256"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"symbol","type":"string"},{"internalType":"address","name":"_mai","type":"address"},{"internalType":"address","name":"_collateral","type":"address"},{"internalType":"address","name":"meta","type":"address"},{"internalType":"string","name":"baseURI","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"vaultID","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"BorrowToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"vaultID","type":"uint256"},{"indexed":false,"internalType":"address","name":"creator","type":"address"}],"name":"CreateVault","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"vaultID","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"DepositCollateral","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"vaultID","type":"uint256"}],"name":"DestroyVault","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"vaultID","type":"uint256"},{"indexed":false,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"address","name":"buyer","type":"address"},{"indexed":false,"internalType":"uint256","name":"debtRepaid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"collateralLiquidated","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"closingFee","type":"uint256"}],"name":"LiquidateVault","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"vaultID","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"closingFee","type":"uint256"}],"name":"PayBackToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"vaultID","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"WithdrawCollateral","type":"event"},{"constant":true,"inputs":[],"name":"_meta","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_minimumCollateralPercentage","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"base","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"baseURI","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"vaultID","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"borrowToken","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"ethPriceSourceAddress","type":"address"}],"name":"changeEthPriceSource","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"vaultID","type":"uint256"}],"name":"checkCollateralPercentage","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"vaultID","type":"uint256"}],"name":"checkCost","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"vaultID","type":"uint256"}],"name":"checkExtract","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"vaultID","type":"uint256"}],"name":"checkLiquidation","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"closingFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"collateral","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"createVault","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"debtRatio","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"vaultID","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"depositCollateral","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"vaultID","type":"uint256"}],"name":"destroyVault","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"ethPriceSource","outputs":[{"internalType":"contract shareOracle","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"vaultID","type":"uint256"}],"name":"exists","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"gainRatio","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getClosingFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getDebtCeiling","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getEthPriceSource","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getOpeningFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"getPaid","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getTokenPriceSource","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"vaultID","type":"uint256"}],"name":"liquidateVault","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"mai","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"maticDebt","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"openingFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"vaultID","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"payBackToken","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"string","name":"baseURI","type":"string"}],"name":"setBaseURI","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"setClosingFee","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"_debtRatio","type":"uint256"}],"name":"setDebtRatio","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"_gainRatio","type":"uint256"}],"name":"setGainRatio","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"minimumCollateralPercentage","type":"uint256"}],"name":"setMinCollateralRatio","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"setOpeningFee","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_pool","type":"address"}],"name":"setStabilityPool","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"_tokenPeg","type":"uint256"}],"name":"setTokenPeg","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"_treasury","type":"uint256"}],"name":"setTreasury","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"stabilityPool","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"tokenPeg","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"}],"name":"transferToken","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountToken","type":"uint256"}],"name":"transferToken","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"treasury","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"vaultCollateral","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"vaultCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"vaultDebt","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"vaultID","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdrawCollateral","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
mai = w3.eth.contract(address=mai_address,
                      abi='[{"constant":false,"inputs":[{"name":"_tokenPeg","type":"uint256"}],"name":"setTokenPeg","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"stabilityPool","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"ethPriceSourceAddress","type":"address"}],"name":"changeEthPriceSource","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"vaultID","type":"uint256"},{"name":"amount","type":"uint256"}],"name":"borrowToken","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"amount","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"closingFee","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"sender","type":"address"},{"name":"recipient","type":"address"},{"name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"vaultOwner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"setClosingFee","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"vaultID","type":"uint256"},{"name":"to","type":"address"}],"name":"transferVault","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"account","type":"address"},{"name":"amount","type":"uint256"}],"name":"mint","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"ethPriceSource","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"createVault","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"treasury","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"account","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_treasury","type":"uint256"}],"name":"setTreasury","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"openingFee","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"vaultID","type":"uint256"},{"name":"amount","type":"uint256"}],"name":"withdrawCollateral","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"vaultID","type":"uint256"},{"name":"amount","type":"uint256"}],"name":"payBackToken","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"vaultID","type":"uint256"}],"name":"destroyVault","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"setOpeningFee","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"isOwner","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getDebtCeiling","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getEthPriceSource","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_pool","type":"address"}],"name":"setStabilityPool","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"account","type":"address"},{"name":"amount","type":"uint256"}],"name":"burn","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"vaultExistence","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getClosingFee","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"vaultCount","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"recipient","type":"address"},{"name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getOpeningFee","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"setDebtCeiling","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"vaultID","type":"uint256"}],"name":"depositCollateral","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[],"name":"erc721","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getTokenPriceSource","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"tokenPeg","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"vaultID","type":"uint256"}],"name":"buyRiskyVault","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"vaultDebt","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"vaultCollateral","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"debtCeiling","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"ethPriceSourceAddress","type":"address"},{"name":"minimumCollateralPercentage","type":"uint256"},{"name":"name","type":"string"},{"name":"symbol","type":"string"},{"name":"vaultAddress","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"previousOwner","type":"address"},{"indexed":true,"name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"vaultID","type":"uint256"},{"indexed":false,"name":"creator","type":"address"}],"name":"CreateVault","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"vaultID","type":"uint256"}],"name":"DestroyVault","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"vaultID","type":"uint256"},{"indexed":false,"name":"from","type":"address"},{"indexed":false,"name":"to","type":"address"}],"name":"TransferVault","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"vaultID","type":"uint256"},{"indexed":false,"name":"amount","type":"uint256"}],"name":"DepositCollateral","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"vaultID","type":"uint256"},{"indexed":false,"name":"amount","type":"uint256"}],"name":"WithdrawCollateral","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"vaultID","type":"uint256"},{"indexed":false,"name":"amount","type":"uint256"}],"name":"BorrowToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"vaultID","type":"uint256"},{"indexed":false,"name":"amount","type":"uint256"},{"indexed":false,"name":"closingFee","type":"uint256"}],"name":"PayBackToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"vaultID","type":"uint256"},{"indexed":false,"name":"owner","type":"address"},{"indexed":false,"name":"buyer","type":"address"},{"indexed":false,"name":"amountPaid","type":"uint256"}],"name":"BuyRiskyVault","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]')
collat_dict = {}
debt_dict = {}

startBlock = w3.eth.get_block_number()
try:
    dposit_filter = liquidator.events.DepositCollateral.createFilter(fromBlock=startBlock)
    withdraw_filter = liquidator.events.WithdrawCollateral.createFilter(fromBlock=startBlock)
    debt_filter = liquidator.events.BorrowToken.createFilter(fromBlock=startBlock)
    repayment_filter = liquidator.events.PayBackToken.createFilter(fromBlock=startBlock)
    vault_filter = liquidator.events.CreateVault.createFilter(fromBlock=startBlock)
    conn = sqlite3.connect(file)
    c = conn.cursor()
    c.execute(create_table)
    conn.commit()
except:
    print('no filters')


print(c.execute("""SELECT * FROM mai_link_vaults""").fetchall())


def createVault(vault):
    try:
        vault_id = vault['args']['vaultID']
        collat_dict.update({vault_id: 0})
        debt_dict.update({vault_id: 0})
        data = [vault_id, collat_dict[vault_id], debt_dict[vault_id]]
        c.execute(create, data)
        print('Vault #' + str(vault_id) + ' created')
    except:
        pass


def dep(deposit):
    try:
        vault_id = deposit['args']['vaultID']
        deposit_value = float(w3.fromWei(deposit['args']['amount'], 'ether'))
        if vault_id in collat_dict:
            collat_dict.update({vault_id: collat_dict[vault_id] + deposit_value})
        else:
            collat_dict.update(({vault_id: deposit_value}))
            debt_dict.update({vault_id: 0})
        data = [vault_id, collat_dict[vault_id], debt_dict[vault_id]]
        c.execute(create, data)
        print('Vault #' + str(vault_id) + " deposited " + str(deposit_value) + ' $LINK')
    except:
        pass


def wit(withdraw):
    try:
        vault_id = withdraw['args']['vaultID']
        withdraw_value = float(w3.fromWei(withdraw['args']['amount'], 'ether'))
        collat_dict.update({vault_id: collat_dict[vault_id] - withdraw_value})
        data = [vault_id, collat_dict[vault_id], debt_dict[vault_id]]
        c.execute(create, data)
        print('Vault #' + str(vault_id) + " withdrew " + str(withdraw_value) + ' $LINK')
    except:
        pass


def deb(debt):
    try:
        vault_id = debt['args']['vaultID']
        debt_value = float(debt['args']['amount'] / 1000000000000000000)
        if vault_id in debt_dict:
            debt_dict.update({vault_id: debt_dict[vault_id] + debt_value})
        else:
            debt_dict.update({vault_id: debt_value})
        data = [vault_id, collat_dict[vault_id], debt_dict[vault_id]]
        c.execute(create, data)
        print('Vault #' + str(vault_id) + " borrowed " + str(debt_value) + ' $MAI')
    except:
        pass


def rep(repay):
    try:
        vault_id = repay['args']['vaultID']
        repay_value = float(repay['args']['amount'] / 1000000000000000000)
        debt_dict.update({vault_id: debt_dict[vault_id] - repay_value})
        data = [vault_id, collat_dict[vault_id], debt_dict[vault_id]]
        c.execute(create, data)
        print('Vault #' + str(vault_id) + " repaid " + str(repay_value) + ' $MAI')
    except:
        pass


def vaultCheck():
    try:
        deposits = dposit_filter.get_all_entries()
        withdraws = withdraw_filter.get_all_entries()
        debts = debt_filter.get_all_entries()
        repayment = repayment_filter.get_all_entries()
        newVaults = vault_filter.get_all_entries()
        endBlock = w3.eth.get_block_number() + 1

    except:
        pass

    if len(deposits) >= 1 or len(withdraws) >= 1 or len(debts) >= 1 or len(repayment) >= 1 or len(newVaults) >= 1:
        vaultChange(deposits=deposits, withdraws=withdraws, debts=debts, repayment=repayment, newVaults=newVaults, endBlock=endBlock)


def vaultChange(deposits, withdraws, debts, repayment, newVaults, endBlock):
    try:
        for x in deposits:
            dep(deposit=x)

        for w in withdraws:
            wit(withdraw=w)

        for d in debts:
            deb(debt=d)

        for r in repayment:
            rep(repay=r)

        for v in newVaults:
            createVault(vault=v)

        conn.commit()

        filterOverwrite(endBlock=endBlock)

    except:
        print('error')


def filterOverwrite(endBlock):
    global dposit_filter
    global withdraw_filter
    global debt_filter
    global repayment_filter
    global vault_filter
    dposit_filter = liquidator.events.DepositCollateral.createFilter(fromBlock=endBlock)
    withdraw_filter = liquidator.events.WithdrawCollateral.createFilter(fromBlock=endBlock)
    debt_filter = liquidator.events.BorrowToken.createFilter(fromBlock=endBlock)
    repayment_filter = liquidator.events.PayBackToken.createFilter(fromBlock=endBlock)
    vault_filter = liquidator.events.CreateVault.createFilter(fromBlock=endBlock)


def getInfo(vault):
    debt = liquidator.functions.vaultDebt(vault).call()
    collat_amount = liquidator.functions.vaultCollateral(vault).call()
    buildData(vault=vault, collat=collat_amount, debt=debt)



def buildData(vault, collat, debt):
    #matic_price = mai.functions.getEthPriceSource().call() / 100000000
    #collat = liquidator.functions.checkCollat(vault).call()
    vault = int(vault)
    mai_debt_value = float(debt)
    link_collat = float(collat)
    link_collat = link_collat/1000000000000000000
    mai_debt = mai_debt_value/1000000000000000000

    collat_dict.update({vault: link_collat})
    debt_dict.update({vault: mai_debt})
    data = [vault, link_collat, mai_debt]
    c.execute(create, data)
    conn.commit()


while True:
    try:
        if len(debt_dict) <= 5:
            for n in range(1, 100):
                getInfo(n)
        vaultCheck()
    except:
        try:
            provider = Web3.WebsocketProvider(choice(url))
            w3 = Web3(provider)
            endBlock = w3.eth.get_block_number() + 1
            filterOverwrite(endBlock=endBlock)
            #print('high level error')
        except:
            print('wtf lol')