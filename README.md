# Wallet Balance Checker
![image](https://github.com/user-attachments/assets/9902e618-7a82-44d1-ac46-785c1d816522)


A Python script to read cryptocurrency wallet addresses from a file, fetch their pending token balances using the ODOS API, and display the results in a user-friendly format.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Error Handling](#error-handling)
- [License](#license)

---

## Features

- **Read Wallets from File:** Supports reading multiple wallet addresses from a text file, each on a new line.
- **Fetch Balances:** Retrieves pending token balances for each wallet using the ODOS API.
- **Formatted Output:** Displays balances in a human-readable format with appropriate decimal places.
- **Error Handling:** Handles common errors such as network issues, invalid wallet addresses, and malformed API responses.

---

## Prerequisites

- **Python 3.6 or higher**
- **pip** (Python package installer)

---

## Installation

1. **Clone the Repository** (or download the script directly):

    ```bash
    git clone https://github.com/Aero25x/odos-claim.git
    cd odos-claim
    ```

2. **Install Required Libraries:**

    The script relies on the `requests` library for making HTTP requests. Install it using pip:

    ```bash
    pip install requests
    ```

3. **Prepare Wallets File:**

    Create a `wallets.txt` file in the project directory. List each wallet address on a separate line:

    ```
    
    0xAnotherWalletAddress
    0xThirdWalletAddress
    ```

---

## Usage

1. **Ensure `wallets.txt` is properly formatted** with one wallet address per line.

2. **Run the Script:**

    ```bash
    python check_balance.py
    ```

3. **View Output:**

    The script will output each wallet address along with its pending token balance, rounded to four decimal places.

---

## Example

**Given `wallets.txt`:**

```

0xAnotherWalletAddress
0xThirdWalletAddress
```

**Running the script:**

```bash
python check_balance.py
```

**Sample Output:**

```
0x01231231321321321 -> 0.9693
0xAnotherWalletAddress -> 123.0000
0xThirdWalletAddress -> 0.0000
```

---

## Error Handling

The script includes error handling for:

- **File Not Found:** If `wallets.txt` is missing, the script will notify the user.
- **Network Issues:** Handles connection errors or timeouts when contacting the API.
- **Invalid Responses:** Checks for correct JSON structure and data types.
- **Invalid Wallet Addresses:** Alerts if the wallet address format is incorrect or not recognized by the API.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

# Проверка Балансов Кошельков

Python-скрипт для чтения адресов криптовалютных кошельков из файла, получения их ожидаемых токен-балансов с использованием API ODOS и отображения результатов в удобном формате.

## Содержание

- [Особенности](#особенности)
- [Требования](#требования)
- [Установка](#установка)
- [Использование](#использование)
- [Пример](#пример)
- [Обработка Ошибок](#обработка-ошибок)
- [Лицензия](#лицензия)

---

## Особенности

- **Чтение Кошельков из Файла:** Поддержка чтения нескольких адресов кошельков из текстового файла, каждый на новой строке.
- **Получение Балансов:** Извлечение ожидаемых токен-балансов для каждого кошелька с использованием API ODOS.
- **Форматированный Вывод:** Отображение балансов в удобочитаемом формате с необходимым количеством десятичных знаков.
- **Обработка Ошибок:** Обработка распространённых ошибок, таких как сетевые проблемы, неверные адреса кошельков и некорректные ответы API.

---

## Требования

- **Python 3.6 или выше**
- **pip** (менеджер пакетов Python)

---

## Установка

1. **Клонируйте Репозиторий** (или скачайте скрипт напрямую):

    ```bash
    git clone https://github.com/Aero25x/odos-claim.git
    cd odos-claim
    ```

2. **Установите Необходимые Библиотеки:**

    Скрипт использует библиотеку `requests` для выполнения HTTP-запросов. Установите её с помощью pip:

    ```bash
    pip install requests
    ```

3. **Подготовьте Файл с Кошельками:**

    Создайте файл `wallets.txt` в директории проекта. Укажите каждый адрес кошелька на отдельной строке:

    ```
    
    0xAnotherWalletAddress
    0xThirdWalletAddress
    ```

---

## Использование

1. **Убедитесь, что `wallets.txt` правильно отформатирован** и содержит один адрес кошелька на строку.

2. **Запустите Скрипт:**

    ```bash
    python check_balance.py
    ```

3. **Просмотрите Вывод:**

    Скрипт выведет каждый адрес кошелька вместе с его ожидаемым токен-балансом, округленным до четырёх десятичных знаков.

---

## Пример

**Дан `wallets.txt`:**

```

0xAnotherWalletAddress
0xThirdWalletAddress
```

**Запуск скрипта:**

```bash
python check_balance.py
```

**Пример Вывода:**

```
 -> 0.9693
0xAnotherWalletAddress -> 123.0000
0xThirdWalletAddress -> 0.0000
```

---

## Обработка Ошибок

Скрипт включает обработку следующих ошибок:

- **Файл Не Найден:** Если отсутствует `wallets.txt`, скрипт уведомит пользователя.
- **Сетевые Проблемы:** Обработка ошибок подключения или таймаутов при обращении к API.
- **Неверные Ответы:** Проверка корректности структуры JSON и типов данных.
- **Неверные Адреса Кошельков:** Уведомление, если формат адреса кошелька неверен или не распознан API.

---

## Лицензия

Этот проект лицензирован под [MIT License](LICENSE).

---

## Скрипт `check_balances.py`

```python
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
```

---

# Дополнительная Информация

Если у вас возникли вопросы или предложения, пожалуйста, создайте [issue](https://github.com/yourusername/wallet-balance-checker/issues) в репозитории или свяжитесь с автором.

---

# Ссылки

- [ODOS API Documentation](https://api.odos.xyz/docs)
- [Python Requests Library](https://requests.readthedocs.io/en/latest/)

---

# Благодарности

Спасибо всем, кто способствовал разработке и улучшению этого проекта!

---

# Contact

For any inquiries, please contact [your.email@example.com](mailto:your.email@example.com).
