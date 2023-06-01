from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


"""
burda selenium kullanarak yazdıgımız uygulamanın testini yaptım.

ilk basta options()u bi options nesnesi haline getirdim. bu nesne kullan-
dığım firefox tarayıcısının yapılandırma seçeneklerini temsil ediyormuş.
Sonra options.headless i false yaptım çünkü headless modu kapatınca 
tarayıcı penceresinin görünmesini istedim. 

bi altındaki kod yani driver=webdrive.firefox(options=options) bu kodda 
firefoxu baslatmak için selenium webdriverın firefox sürücüsünü kullandım 

sonra webdirverin verdigim urle gidip web sayfasını yüklemesini söyledim
bu url de zaten flaskın uygulamamızın urli.
"""
options = Options()

options.headless = False
driver = webdriver.Firefox(options=options)
driver.get('http://127.0.0.1:5000')

cities = ['Dubai', 'Şırnak', 'Los Angeles', 'London', 'New York']
"""
cities içerisine farklı 5 şehir ekledim. for döngüsü kurdum. bu döngüde 
find_element() ile sayfada name özelliği city olan bi giris alanı bul dedim
bu giriş alanı havadurumu appinin şehir girişi için kullanıan alanı temsil 
eder. 
sonra time.sleep koydum
sonra clear ile şehir adını sildim. if ekledim burda tr karakter varmı yokmu
kontrolü yaptırdım. varsa hata mesajı yazdırdım. continue ile devam dedim. 
ifden cıkınca yeni şehir adını yolladım  city_input.send_keys(city) bu
kodu kullanarak sonra enter tusuna bastıran kodu yazdırdım enter tusuna
basarak sehir adını onaylattım ve havadurumu verilerinin getirilmesini sagladım

bi time.sleep daha attım
country_code = driver.find_element(By.ID, 'country_code').text bunu kullandım
bu kodla verilen ID degerine sahip ogeyi yani country_code u buldu ve onun 
içindeki metni aldı. yani ülke kodunu aldı. 
aynı şekilde diğer ogeleri buldu v eonların içindeki metinleri aldı. 
yani havadurumu verilerinin alanlarının verilerini aldı. 

data diye liste oluşturup bunları doldurdu. bunları printledim.
bunları döngü halinde yaptırıp driverı kapattırdım.

"""
for city in cities:
    city_input = driver.find_element(By.NAME, 'city')
    time.sleep(1)
    city_input.clear()
    if any(char in city for char in 'çÇşŞğĞüÜöÖıİ'):
        print(f"\n'{city}' şehri için Türkçe karakter tespiti. HATALI! \n\n")
        continue

    city_input.send_keys(city)
    city_input.send_keys(Keys.RETURN)
    time.sleep(2)
    country_code = driver.find_element(By.ID, 'country_code').text
    coordinate = driver.find_element(By.ID, 'coordinate').text
    temp = driver.find_element(By.ID, 'temp').text
    temp_cel = driver.find_element(By.ID, 'temp_cel').text
    pressure = driver.find_element(By.ID, 'pressure').text
    humidity = driver.find_element(By.ID, 'humidity').text
    cityname = driver.find_element(By.ID, 'cityname').text

    data = [
        ('Ülke Kodu', country_code),
        ('Koordinat', coordinate),
        ('Sıcaklık', temp),
        ('Sıcaklık (Celsius)', temp_cel),
        ('Basınç', pressure),
        ('Nem', humidity),
        ('Şehir Adı', cityname)
    ]

    print(f'Hava Durumu Bilgileri - {city}')
    for label, value in data:
        print(label + ':', value)

    print('-' * 30)

time.sleep(3)
driver.quit()
