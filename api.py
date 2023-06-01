from flask import Flask, render_template, request
import re
from config import settings
import requests

"""
flask web uygulamasını oluşturdum. app adında flask uygulaması nesnesi oluşturdum
app yaptıgım uygulamanın temelini oluşturacak. flask uygulamasını oluşturmak 
için bu kodu kullanabiliriz. app nesnesini geliştirip istediğimiz uygulamayı 
oluşturucağım
"""
app = Flask(__name__)

"""
bu kod ile data içerisindeki kelvin cinsindeki sıcaklık değerini celciusa dönüştürdüm
temp olarak aldıgım degeri float tipine dönüştürdüm. -273,16 yaptım
sonra 2 ondalık basamaklı sayıya döndürdüm cıkan sonucu kullandım
"""
def to_celcius(temp):
    return str(round(float(temp) - 273.16, 2))


"""
bu kodda hava durumu tahminlerini almak için api'ye istek yaptım 
city parametresindeki şehir ismini aldım. bu şehrin degerlerini almak için 
api cagrısı yaptım. settingsdeki api_key ve url i kullandım. 
response kullandım apiden gelen yanıtı aldım. json formatına dönüştürdüm ve 
return ettim
"""
def get_weather_forecast(city):
    api_key = settings.api_key
    url = settings.url + city + '&appid=' + api_key
    response = requests.get(url)
    return response.json()


"""
şimdi web sunucusu başlatıcağız. 
burda "/" yolu için GET ve POST isteklerini yönlendiren bi işlev tanımladım
bu ifadeyle flask uygulamasında bir yönlendirme (route) oluşturdum
sonra türkçe regex ekleyerek türkçe karakterleri tespit etmek için kullandık
kontrol işlemleri yaptım.

istek methodu POST ise request.form üzerinden cityyi aldım
istek methodum POST degilse varsayılan olarak istanbul yaptım. 
  
city içerisinde tr karakter var ise index.html ile 
error yanıtı renderladım burda uyarıda bulundum. 

tr karakter sorunu yok ise yukarıda oluşturdugum get_weather_forecast(city)yi
kullanıp citynin hava durumu tahminlerini aldım. Sonra bu city api ile
aldıgım datada yoksa hata mesajım ile birlikte index.htmli renderladım.

data içerisinde verdigim city kodu var ise verileri data sözcüğüne topladım
sonra da index.html i ve data sözcüğünü ilettim kullanıcıya verileri 
gösterdim. 
"""
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
    """
    burda flaskın calıstıgı web sunucusunu baslattım. 
    debug=True ile hata ayıklama modunu etkinleştirdim. eger kodda sıkıntı
    varsa hata mesajı versin diye. 
    """
    app.run(debug=True)
