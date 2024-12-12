import requests

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

    for wallet in wallets:
        balance = get_balance(wallet)
        if balance is not None:
            print(f"{wallet} -> {round(balance, 4)}")

if __name__ == "__main__":
    main()
