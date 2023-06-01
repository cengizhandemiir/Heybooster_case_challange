from pydantic import BaseModel

"""
burda api_keyi str olarak tanımladım api_keyi buraya koydum. 
urli de str olarak tanımladım burda pydantic kullanarak Settings sınıfını olusturdum. yapılandırma 
degerlerinin gecerli olup olmadıgını kontrol etmek ve uygulamanın beklenen veri yapısına uygun olarak 
calısmasını saglamak için ekledim. büyük projelerde işlemi kolaylaştıran bi kütüphane.
"""
class Settings(BaseModel):
    api_key: str
    url: str
settings = Settings(api_key='48a90ac42caa09f90dcaeee4096b9e53', url='http://api.openweathermap.org/data/2.5/weather?q=')
