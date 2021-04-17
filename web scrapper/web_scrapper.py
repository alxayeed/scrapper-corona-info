from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

source = requests.get('http://quotes.toscrape.com/').text
soup = BeautifulSoup(source, 'lxml')
# get quote text
quote = soup.find('div', class_='quote')
quote_text = quote.span.text
# get author
author = soup.find('small', class_='author').text


@app.route('/')
def home():
    return render_template('index.html', quote=quote_text, author=author)


if __name__ == '__main__':
    app.run(debug=True)
