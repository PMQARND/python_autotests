import requests
import pytest

url_api = 'https://api.pokemonbattle.me/v2' 
headers_api = {'Content-Type' : 'application/json'}
token = '027a2abe0a6d8e3ef1ba24859f891fe2' #сюда вводим свой токен
trainer_id = 2043 #cюда вводим id своего тренера

def test_status_code():
    response = requests.get(url = f'{url_api}/trainers', params = {'level' : 1} )
    assert response.status_code == 200 #проверяем, что статус ответа равняется 200

def test_name_trainer():
    response = requests.get(url = f'{url_api}/trainers', params = {'trainer_id' : trainer_id} )
    assert response.json()['data'][0]['trainer_name'] == 'ZmeyaTest'  #проверяем, что имя тренера равняется ZmeyaTest

CASES = [
    ('city', 'RnD'),
    ('trainer_name', 'ZmeyaTest'),
]    

@pytest.mark.parametrize('key, value', CASES)

def test_parametrize_body(key, value):
    response = requests.get(url = f'{url_api}/trainers', params = {'trainer_id' : trainer_id} )
    assert response.json()['data'][0][key] == value
