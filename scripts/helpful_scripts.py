from brownie import network, config, accounts, MockV3Aggregator

LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache-local"]


DECIMALS = 8
STARTING_PRICE = 200000000000


def get_accounts():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_accounts()})
    print("Mocks Deployed successfully")


def main():
    deploy_mocks()
    # get_price()
    # withdraw()
