"""
Поиск фидьма на Кинопоиске по названию
"""
import requests
import json
import urllib.parse

url = "https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=10&query="

headers = {
    "accept": "application/json",
    "X-API-KEY": "QP6ETYP-73V4A0H-MTDRYZ4-WMX96PM"
}

name = input('Ввыедите название фильма: ')

params = {
    'name': name
}


response = requests.get(url + urllib.parse.quote(name.encode('utf8')), params=params, headers=headers)

# print(response.text)

if response.status_code == 200:
    print("Успешный запрос API!")
    data = json.loads(response.text)
    venues = data["docs"]
    for venue in venues:
        print("Название:", venue["name"])
        print("Описание:", venue["description"])
        print("Рейтинг:", venue["rating"])
        print("\n")
else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)