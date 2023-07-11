import requests

#res = requests.put(url, data=data)

params = {
  'status': 'available'
}

headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

data = {
  "id": 0,
  "username": "bibaboba",
  "firstName": "Biba",
  "lastName": "Boba",
  "email": "biba@bobamail.ru",
  "password": "Bob@task12",
  "phone": "89999999090",
  "userStatus": 0
}

res2 = requests.put(f'https://petstore.swagger.io/v2/user/bibaboba', json=data)

print(res2.status_code)
print(res2.text)
print(res2.json())
print(type(res2.json()))