import requests
import time

url_api = 'https://api.pokemonbattle.me/v2' 
headers_api = {'Content-Type' : 'application/json'}
token = '027a2abe0a6d8e3ef1ba24859f891fe2' #тут вводим свой токен
my_email = 'testov_email@email.test' #тут вводим свой e-mail
my_password = 'Iloveqa1' #тут вводим свой пароль
headers_api_pok = {'Content-Type': 'application/json', 'trainer_token': token}


body = {
    'trainer_token': token, 
    'email': my_email,
    'password': my_password 
}

body_confirm = {
    'trainer_token': token
}

body_create_pok = {
    "name": "generate",
    "photo": "generate"
}

print("")
print("---Запуск консоли PokemonBattle---")
time.sleep(0.5)
print("")
while True:
 response = input("""
!!!ВНИМАНИЕ!!! Функционал минимальный, поэтому некоторые функции буду работаь некорректно, если их выполнять не поочередно !!!ВНИМАНИЕ!!!
- Введите 1 — чтобы создать/зарегистрировать тренера
- Введите 2 — чтобы подтвердить E-mail
- Введите 3 — чтобы создать покемона и записать его ID в переменную
- Введите 4 — чтобы сменить имя покемона                                                  
- Введите 5 — чтобы поймать покемона в покебол  
- Введите 0, либо Exit — чтобы выключить функционал консоли                              
""")

 # Проверка введенного значения
 if response.lower() in ["1", "один", "one"]:
    print("Создаём/регистрируем тренера")

    response = requests.post(url = f'{url_api}/trainers/reg', headers = headers_api, json = body) #регистрация/создание тренера
    print(response.text, f"\nСтатус код ответа: {response.status_code}")

 elif response.lower() in ["2", "два", "two"]:
    print("Подтверждение E-mail")

    response_confirm_email = requests.post(url = f'{url_api}/trainers/confirm_email', headers = headers_api, json = body_confirm) #подтверждение e-mail
    print(response_confirm_email.text, f"\nСтатус код ответа: {response_confirm_email.status_code}")

 elif response.lower() in ["3", "три", "three"]:
    print("Создаём покемона и записываем его ID в переменную")

    response_create_pok = requests.post(url = f'{url_api}/pokemons', headers = headers_api_pok, json = body_create_pok) #создание покемона
    print(response_create_pok.text, f"\nСтатус код ответа: {response_create_pok.status_code}")

    response_json = response_create_pok.json()
    id = response_json.get("id") #записываем значение ключа id из ответа - в переменную id питона

 elif response.lower() in ["4", "четыре", "four"]:
    print("Смена имени у недавно созданного с помощью данной консоли покемона")
    
    body_rename_pok = {
    "pokemon_id": id,
    "name": "SmenaImeniPok",
    }

    response_rename_pok = requests.patch(url = f'{url_api}/pokemons', headers = headers_api_pok, json = body_rename_pok) #смена имени покемона
    print(response_rename_pok.text, f"\nСтатус код ответа: {response_rename_pok.status_code}")

 elif response.lower() in ["5", "пять", "five"]:
    print("Поймать недавно созданного с помощью данной консоли покемона")
     
    body_add_pokeball_pok = {
    "pokemon_id": id
    }

    response_add_pokeball_pok = requests.post(url = f'{url_api}/trainers/add_pokeball', headers = headers_api_pok, json = body_add_pokeball_pok) #поймать покемона в покебол
    print(response_add_pokeball_pok.text, f"\nСтатус код ответа: {response_add_pokeball_pok.status_code}")

 elif response.lower() in ["0", "ноль", "нуль", "exit"]:
    print("Функционал консоли выключен")
    break
 
 else:
    print("")
    print("Неверный ввод. Пожалуйста, попробуйте снова")
    time.sleep(1)