# Heybooster-my-case
 Hava Durumu Uygulaması

Bu Flask uygulaması, kullanıcının hava durumu bilgilerini arama ve görüntüleme imkanı sunar. Kullanıcı, web formu aracılığıyla bir şehir adı girer ve uygulama bu şehir için hava durumu tahminlerini sağlar.
Başlangıç

Uygulamayı çalıştırmadan önce, aşağıdaki adımları takip ederek gerekli ayarları yapmanız gerekmektedir:

    config adlı bir Python paketi oluşturun ve içine settings.py adında bir dosya yerleştirin. Bu dosya, hava durumu API'si için gereken yapılandırma ayarlarını içerecektir.

    settings.py dosyasına aşağıdaki örnek içeriği ekleyin:

python

# settings.py

api_key = 'YOUR_API_KEY'  # Hava durumu API anahtarını buraya girin
url = 'https://api.openweathermap.org/data/2.5/weather?q='

    Not: YOUR_API_KEY yerine, OpenWeatherMap API anahtarınızı sağlamalısınız. OpenWeatherMap API'ye kaydolup, bir API anahtarı almanız gerekmektedir.

Kullanım

    Flask uygulamasını çalıştırın:

bash

python app.py

    Tarayıcınızı açın ve http://127.0.0.1:5000 adresine gidin.

    Web formunda bir şehir adı girin ve "Gönder" düğmesine tıklayın.

    Uygulama, hava durumu tahminlerini getirerek bu bilgileri ekranda görüntüler.

Fonksiyonlar
to_celsius(temp)

Bu fonksiyon, Kelvin cinsinden verilen sıcaklık değerini Celsius'a dönüştürür.

Parametre:

    temp: Kelvin cinsinden sıcaklık değeri

Dönüş Değeri:

    Celsius cinsinden sıcaklık değeri (string)

get_weather_forecast(city)

Bu fonksiyon, belirtilen şehir için hava durumu tahminlerini alır.

Parametre:

    city: Hava durumu tahminlerini almak istediğiniz şehir adı

Dönüş Değeri:

    JSON formatında hava durumu tahminlerini içeren bir yanıt

Route'lar
/

Bu route, ana sayfayı temsil eder. HTTP GET ve POST isteklerini kabul eder.

GET İsteği:

    Eğer city parametresi boşsa, varsayılan olarak "Istanbul" şehri için hava durumu bilgilerini getirir.
    Eğer city parametresi doluysa, belirtilen şehir için hava durumu bilgilerini getirir.

POST İsteği:

    Web formunda girilen şehir adıyla hava durumu bilgilerini getirir.

Dönüş Değeri:

    Eğer şehir bulunamazsa veya Türkçe karakter kullanılırsa, hata mesajı içeren HTML şablonunu döndürür.
    Aksi takdirde, hava durumu bilgilerini içeren HTML şablonunu döndürür.
