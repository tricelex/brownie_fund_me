from brownie import FundMe
from scripts.helpful_scripts import get_accounts


def fund():
    fund_me = FundMe[-1]
    account = get_accounts()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding the contract...")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_accounts()
    fund_me.withdraw({"from": account})


def get_amount_funded():
    fund_me = FundMe[-1]
    account = get_accounts()
    funders = fund_me.funders()
    print(f"The list of funders is {funders}")


def get_price():
    fund_me = FundMe[-1]
    # account = get_accounts()2000000000000000000000
    price = fund_me.getConversionRate(1)
    print(price)
    print(f"The current price is {price}")


def main():
    fund()
    withdraw()
    # get_amount_funded()
    # get_price()
