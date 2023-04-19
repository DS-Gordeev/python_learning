import requests

json = {
  "head": {
    "sid": "",
    "wid": "",
    "cid": "",
    "bean": "",
    "method": ""
  },
  "body": {
    "username": "",
    "password": "",
    "platformUniqueKey": "fa4b4628-c8be-6ecd-e5bf-8b2301029c57",
    "platform": "Win32",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0 (Edition Yx 05)",
    "frontTime": "2023-04-19T16:33:13.000+0300",
    "methodName": "ESIA"
  }
}


req = requests.post('https://dev.ppdp.ru/lkWS/sinc', json=json)
print(req.status_code)
print(req.json())
print(req.json()['data']['sid'])
sid = req.json()['data']['sid']

json_2 = {
  "login": "+7 (916) 325-43-69",
  "password": "Knopka023456!"
}
req_2 = requests.post('https://esia-portal1.test.gosuslugi.ru/aas/oauth2/api/login', json=json_2)
print(req_2.status_code)
print(req_2.json())


json_3 = {
  "head": {
    "sid": "28f7ca07-88de-4a2d-b139-c93c8361095e",
    "wid": "",
    "cid": "",
    "bean": "lk",
    "method": "saveUserLk"
  },
  "body": {
    "user": {
      "key": "null",
      "personKey": 11881,
      "department": "null",
      "position": "null",
      "entityKey": "null",
      "entityTypeId": "null",
      "phone": "+79163254369",
      "email": "forautotests@mail.ru",
      "surname": "Хан",
      "forename": "Наталия",
      "patronymic": "ивановна",
      "inn": "null",
      "snils": "46138428389"
    }
  }
}

for i in range(1):
  req_3 = requests.post('https://dev.ppdp.ru/lkWS/sinc?saveUserLk', json=json_3)
  print(req_3.status_code)
  print(req_3.json())