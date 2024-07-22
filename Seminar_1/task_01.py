# Задание 1
# Семинар 1. Сбор и разметка данных
# - использовать библиотеку requests в Python для отправки
# запросов GET, POST, PUT и DELETE на конечную точку REST API
# https://jsonplaceholder.typicode.com/posts/1.
# - использовать методы requests.get(), requests.post(),
# requests.put() и requests.delete() для отправки соответствующих
# HTTP-запросов.
# - проверить код состояния ответа и вывести текст ответа, если
# запрос был успешным.

import requests

url = 'https://jsonplaceholder.typicode.com/posts'

# отправка GET-запроса на конечную точку REST API
response = requests.get(url + '/1')

# проверка успешности выполнения запроса
if response.status_code == 200:
    print("Успешный запрос!")
    # вывод текста ответа
    print(response.text)
else:
    print("Запрос не удался с кодом состояния:", response.status_code)

# отправка POST-запроса на конечную точку REST API
data = {
    "title": "Hello!",
    "body": "Scraping",
    "userId": 1
}

response = requests.post(url, json=data)

# проверка успешности выполнения запроса
if response.status_code == 201:
    print("Успешный запрос!")
    # вывод текста ответа
    print(response.text)
else:
    print("Запрос не удался с кодом состояния:", response.status_code)

payload = {"field1": "value1", "field2": "value2"}
response = requests.put(url + '/1', json=payload)

# проверка успешности выполнения запроса
if response.status_code == 200:
    print("Успешный запрос!")
    # вывод текста ответа
    print(response.text)
else:
    print("Запрос не удался с кодом состояния:", response.status_code)

response = requests.delete(url + '/1')

# проверка успешности выполнения запроса
if response.status_code == 200:
    print("Успешный запрос!")
    # вывод текста ответа
    print(response.text)
else:
    print("Запрос не удался с кодом состояния:", response.status_code)