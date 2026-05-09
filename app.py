from flask import Flask
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")

BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"


@app.route("/")
def home():

    from_currency = "USD"

    to_currency = "INR"

    amount = 1

    url = BASE_URL + from_currency

    response = requests.get(url)

    data = response.json()

    rate = data["conversion_rates"][to_currency]

    converted_amount = round(amount * rate, 2)

    return f"{amount} {from_currency} = {converted_amount} {to_currency}"


if __name__ == "__main__":
    app.run(debug=True)