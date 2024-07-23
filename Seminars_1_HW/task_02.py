# Сценарий Foursquare
# Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию (например, кофейни, музеи, парки и т.д.).
# Используйте API Foursquare для поиска заведений в указанной категории.
# Получите название заведения, его адрес и рейтинг для каждого из них.
# Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.

import requests
import json

client_id = "__"
client_secret = "__"

endpoint = "https://api.foursquare.com/v3/places/search"

place =input("Введите категорию места (например, кофейни, музеи, парки и т.д.): ")

params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "query": place
}

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3V3AFHzvqod5PVkb9j5ptfec29VfLTGG2XbHrQEGC8bI="
}

response = requests.get(endpoint, params=params, headers=headers)
print(response.text)
# Проверка успешности запроса API
if response.status_code == 200:
    print("Успешный запрос API!")
    data = json.loads(response.text) # Парсим JSON-ответ в словарь Python
    venues = data["results"] # Получаем список мест из данных ответа
    for venue in venues:# Проходимся по каждому месту в списке
        print("Город:", venue["location"]["locality"])
        print("Название:", venue["name"])
        try:
            print("Адрес:", venue["location"]["address"])
        except Exception:
            print("Адрес не найден:")
        print("\n")
else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)