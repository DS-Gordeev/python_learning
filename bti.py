import requests


for i in range(300, 401):
    url = f'https://mosgorbti.com/get-order-info/pdf/{i}/'
    req = requests.get(url)
    with open(f'./downloadedFiles/{i}.pdf', 'wb') as f:
        f.write(req.content)
