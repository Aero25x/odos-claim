import requests


print("""



  _    _ _     _     _             _____          _
 | |  | (_)   | |   | |           / ____|        | |
 | |__| |_  __| | __| | ___ _ __ | |     ___   __| | ___
 |  __  | |/ _` |/ _` |/ _ \ '_ \| |    / _ \ / _` |/ _ \\
 | |  | | | (_| | (_| |  __/ | | | |___| (_) | (_| |  __/
 |_|  |_|_|\__,_|\__,_|\___|_| |_|\_____\___/ \__,_|\___|

                Odos Checker by Aero25x

Dont forget add stars for repo - https://github.com/Aero25x/odos-claim/
    """)



def read_wallets(file_path):
    """Читает кошельки из файла, удаляя пробелы и пустые строки."""
    try:
        with open(file_path, 'r') as file:
            wallets = [line.strip() for line in file if line.strip()]
        return wallets
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []

def get_balance(wallet):
    """Получает баланс для указанного кошелька через API."""
    url = f"https://api.odos.xyz/loyalty/users/{wallet}/balances"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на HTTP-ошибки
        data = response.json()

        # Извлечение баланса
        pending_balance_str = data.get("data", {}).get("pendingTokenBalance", "0")
        pending_balance = int(pending_balance_str)
        actual_balance = pending_balance / 10**18

        return actual_balance
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса для кошелька {wallet}: {e}")
    except ValueError:
        print(f"Неверный формат баланса для кошелька {wallet}.")
    except KeyError:
        print(f"Некорректный ответ от API для кошелька {wallet}.")
    return None

def main():
    wallets_file = 'wallets.txt'  # Имя файла с кошельками
    wallets = read_wallets(wallets_file)

    if not wallets:
        print("Нет кошельков для обработки.")
        return


    total_balance = 0

    for wallet in wallets:
        balance = get_balance(wallet)
        if balance is not None:
            total_balance +=balance
            print(f"{wallet} -> {round(balance, 4)}")


    print(f"TOTAL: {total_balance}")

if __name__ == "__main__":
    main()
