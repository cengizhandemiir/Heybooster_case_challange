from flask import Flask, render_template, request
import re
from config import settings
import requests

app = Flask(__name__)


def to_celcius(temp):
    return str(round(float(temp) - 273.16, 2))


def get_weather_forecast(city):
    api_key = settings.api_key
    url = settings.url + city + '&appid=' + api_key
    response = requests.get(url)
    return response.json()


@app.route('/', methods=['POST', 'GET'])
def weather():
    turkce_regex = r"[çÇşŞğĞüÜöÖıİ]"

    if request.method == 'POST':
        city = request.form['city']

    else:
        city = 'Istanbul'

    turkce_karakterler = re.findall(turkce_regex, city)
    if len(turkce_karakterler) > 0:
        return render_template('index.html', err="Türkçe karakter kullanmayınız. "
                                                 "Gireceğiniz şehri ingilizce kelimeler ile yazınız!")

    else:

        list_of_data = get_weather_forecast(city)

        if int(list_of_data["cod"]) != 200:
            return render_template('index.html', err="Böyle bir şehir bulunamadı. Tekrar deneyin.")

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "temp_cel": to_celcius(list_of_data['main']['temp']) + 'C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "cityname": str(city),
        }
        return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
