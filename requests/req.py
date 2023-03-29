import requests
import pytest
def test_my():
    req = requests.get('https://api.openbrewerydb.org/v1/breweries/ef970757-fe42-416f-931d-722451f1f59c')
    print(req.status_code)
    print(req.json())
    assert req.status_code == 200, 'Статус-код не соответствует 200'
    assert req.json()['id'] == 'ef970757-fe42-416f-931d-722451f1f59c!', 'ID пивоварни не соответствует запрошиваемому'

