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
total_case = data[0].div.span.text

# find total deaths
total_death_title = data[1].h1.text
total_death = data[1].div.span.text

# find total recovered
total_recovered_title = data[2].h1.text
total_recovered = data[2].div.span.text


# strip commas and convert to int
total_recovered_int = int(total_recovered.strip().replace(',', ''))
total_case_int = int(total_case.strip().replace(',', ''))

# percentage of recovery
recovery_percentage = total_recovered_int / total_case_int * 100
# take 2 decimal places
recovery_percentage = f'{recovery_percentage:.2f}'


@app.route('/dashboard')
def home():
    return render_template('home.html', total_case=total_case, total_death=total_death, total_recovered=total_recovered, recovery_percentage=recovery_percentage)


if __name__ == "__main__":
    app.run(debug=True)
