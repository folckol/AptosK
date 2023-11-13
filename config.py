node_url = "https://fullnode.mainnet.aptoslabs.com/v1"

tokens_mapping = {
    "APT": "0x1::aptos_coin::AptosCoin",
    "USDT": "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDT",
    "USDC": "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC",
}

# Если хотите, чтобы в логах был баланс до свапа ставьте True, если нет, то False
show_balance_before_swap = True
# Если хотите, чтобы в логах был баланс после свапа ставьте True, если нет, то False
show_balance_after_swap = True
# Если хотите рандомизировать кошельки, то ставьте True, если нет, то False
randomize_wallets = True
# Если хотите делать паузы между кошельками, то ставьте True, если нет, то False
is_sleep = True
# Количество секунд паузы между кошельками
sleep_from = 15
sleep_to = 20
# Количество секунд паузы между кошельками
from_token = 'APT'
to_token = 'USDT'
# from_token = 'USDT'
# to_token = 'APT'
from_amount = 0.001
to_amount = 0.002
# Количество секунд паузы между кошельками
apto_swap_executions_left = 0
liquid_swap_client_executions_left = 2
pancake_swap_client_executions_left = 2
