from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

url = 'https://www.worldometers.info/coronavirus/'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

# find all div with id maincounter-wrap
data = soup.find_all("div", id="maincounter-wrap")

# find total cases
total_case_title = data[0].h1.text
total_case = int(data[0].div.span.text.strip().replace(',', ''))

# find total deaths
total_death_title = data[1].h1.text
total_death = int(data[1].div.span.text.strip().replace(',', ''))

# find total recovered
total_recovered_title = data[2].h1.text
total_recovered = int(data[2].div.span.text.strip().replace(',', ''))

# percentage of recovery
recovery_percentage = total_recovered / total_case * 100
print(f'{recovery_percentage:.2f}')

if __name__ == "__main__":
    app.run(debug=True)
