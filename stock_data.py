import requests
from bs4 import BeautifulSoup
import sys

def get_price(stock_symbol : str) -> str:

    url = f"https://finance.yahoo.com/quote/{stock_symbol}"

    response = requests.get(url, headers={'Cache-Control': 'no-cache'})

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        stock_price = soup.find('fin-streamer', class_='Fw(b) Fz(36px) Mb(-4px) D(ib)').text
        return stock_price
    else:
        raise ValueError

if __name__ == "__main__":
    main()
