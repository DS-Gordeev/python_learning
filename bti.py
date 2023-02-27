import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup



# for i in range(300, 401):
#     url = f'https://mosgorbti.com/get-order-info/pdf/{i}/'
#     req = requests.get(url)
#     with open(f'./downloadedFiles/{i}.pdf', 'wb') as f:
#         f.write(req.content)

# url = f'https://mosgorbti.com/get-order-info/7979/'
# req = requests.get(url)
# full_text = req.text



url = "https://mosgorbti.com/get-order-info/7979/"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)


