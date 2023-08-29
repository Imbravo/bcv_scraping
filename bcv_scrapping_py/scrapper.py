import requests
from bs4 import BeautifulSoup


def get_bcv():
    url = 'https://www.bcv.org.ve/'
    data = requests.get(url)

    if data is not None:
        html = BeautifulSoup(data.text, 'html.parser')
        div = html.find(id="dolar")
        usd = div.select('strong')[0].get_text()
        usd = usd.replace(',', '.')
        return {"usd": float(usd)}
    else:
        return 'empty'

