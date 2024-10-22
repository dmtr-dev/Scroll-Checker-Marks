import requests
import time
from ctypes import windll
from termcolor import cprint

with open("wallets.txt", "r") as file:
    addresses_list = file.read().splitlines()

def get_wallet_points(address):
    try:
        response = requests.get(f"https://www.data-openblocklabs.com/scroll/wallet-points?walletAddress={address}")
        response.raise_for_status()
        data = response.json()
        marks = data[0].get("points", 0)
        return marks
    except Exception as error:
        cprint(f"{address} | Error: {error}", 'red')
    return None

for address in addresses_list:
        marks = get_wallet_points(address)
        if marks is not None and marks >= 200:
            cprint(f"{address} | {marks}", 'blue')
        time.sleep(5)

if __name__ == "__main__":
    windll.kernel32.SetConsoleTitleW('Scroll Checker Marks | by https://t.me/dmtrcrypto')
    cprint("\nTG Channel - https://t.me/dmtrcrypto\n\n", 'magenta')
