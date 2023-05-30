from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()

options.headless = False
driver = webdriver.Firefox(options=options)
driver.get('http://127.0.0.1:5000')

cities = ['Dubai', 'Şırnak', 'Los Angeles', 'London', 'New York']

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
