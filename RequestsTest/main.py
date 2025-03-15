import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '4a5b99f7d88d3280ca5e8740f0e5f875'
HEADER = {'Content-Type':'application/json', 'trainer token':TOKEN}

body_registration = {
    "trainer_token":TOKEN,
    "email":"User_login",
    "password":"User_password"
}


body_create = {
    "name": "Бульбазавр",
    "photo" : "https://dolnikov.ru/pokemons/albums/001.png"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)	
print(response_create.text)
