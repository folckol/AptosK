import random
import time
import traceback

from loguru import logger
import concurrent.futures
from liquidswap.client import LiquidSwapClient
from pancakeswap.client import PancakeSwapClient
from aptoswap.client import AptoSwap
from config import node_url, tokens_mapping, show_balance_before_swap
from config import randomize_wallets, sleep_from, sleep_to
from config import from_token, to_token, from_amount, to_amount
from config import apto_swap_executions_left, liquid_swap_client_executions_left, pancake_swap_client_executions_left


def ex(dex: [AptoSwap, LiquidSwapClient, PancakeSwapClient]) -> None:
    if dex.executions_left > 0:
        dex.client_config.max_gas_amount = 5_000
        amount = round(random.uniform(from_amount, to_amount), 8)

        try:
            if show_balance_before_swap:
                logger.info(f"Баланс {from_token}: {dex.get_token_balance(from_token)}; "
                            f"Баланс {to_token}: {dex.get_token_balance(to_token)}")

            coins_in = dex.calculate_rates(from_token, to_token, amount)
            coins_out = dex.calculate_rates(to_token, from_token, coins_in)

            logger.warning(f"Попытка свапнуть {coins_out} {from_token} в {coins_in} {to_token}")
            dex.swap(from_token, to_token, amount, coins_in)
            time.sleep(random.randint(sleep_from, sleep_to))
            dex.executions_left -= 1
        except Exception:
            dex.executions_left -= 1


def random_execution(class_instances: list) -> None:
    methods = []
    for class_instance in class_instances:
        num_executions = class_instance.executions_left
        for _ in range(num_executions):
            methods.append((class_instance, ex))
    random.shuffle(methods)
    for class_instance, method in methods:
        method(class_instance)


def main():
    with open('wallets.txt', 'r', encoding='utf-8-sig') as file:
        wallets = [line.strip() for line in file]

    if randomize_wallets:
        random.shuffle(wallets)

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for wallet in wallets:
            apto_swap = AptoSwap(node_url, tokens_mapping, wallet, apto_swap_executions_left)
            liquid_swap_client = LiquidSwapClient(node_url, tokens_mapping, wallet, liquid_swap_client_executions_left)
            pancake_swap_client = PancakeSwapClient(node_url, tokens_mapping, wallet,
                                                    pancake_swap_client_executions_left)

            class_instances = [apto_swap, pancake_swap_client, liquid_swap_client]

            future = executor.submit(random_execution, class_instances)
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            future.result()


if __name__ == "__main__":

    try:
        print(' ___________________________________________________________________\n'
              '|                       Rescue Alpha Soft                           |\n'
              '|                   Telegram - @rescue_alpha                        |\n'
              '|                   Discord - discord.gg/438gwCx5hw                 |\n'
              '|___________________________________________________________________|\n\n\n')

        for i in range(30):
            main()

    except:
        traceback.print_exc()
        input()
