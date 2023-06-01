import unittest
from flask_testing import TestCase
from api import app
"""
appimizin test senaryolarını içeren bi test sınıfı actık
"""
class WeatherTestCase(TestCase):
    """
    create_app ile appin test modunda calısmasını sagladım. sonra app.config[TESTING]testing_true
     yaparak test modunda oldugunu belirttim.
    """
    def create_app(self):
        app.config['TESTING'] = True
        return app
    """
    test_turkish_characters metoduyla türkçe karakterlerin kullanıldıgı sehir edı göndererek appin tepkisini
    test ettim. cityye şırnakı verdim status kodunu kontrol ettim ve beklenen degeri 200 e eşlenip 
    eşlenmedigini kontrol ettim. 200 degilse test basarısızdır. 
    şırnak girildiginde türkçe karakter kullanmayınız ifadesi bulunup bulunmadıgını kontrol ettirdim.
    response.data.decode('utf-8') bu ifadeyle yanıtın içerigini utf-8 karakter kodlamasından
    unicode metne dönüstürdü. eğer metin yanıtının içinde bulunmuyosa test basarısız demektir.
    
    """
    def test_turkish_characters(self):
        response = self.client.post('/', data={'city': 'Şırnak'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Türkçe karakter kullanmayınız', response.data.decode('utf-8'))

    """
    bu metotda gererli bir şehir verdim (mexico) bu şehri appe göndererek dogru tepki veriyo mu diye 
    test ettik 
    yine status kodu kontrol ettik. 200 ile eşlenip eşlenmedigine baktık
    assertNotIn ile "türkçe karakter kulanmayınız" ifadesinin olmadıgını dogruladık. utf-8 li kod ile de 
    yanıt içerigini utf-8 karakter kodlamasında unicode metne dönüştürdük. eğer belirtilen metin yanıtın
    içinde bulunursa test basarısız olur. 
    assertIn li kodda da mexico metnin bulunup bulunmadıgını test ettim. 
    asıl amac su bu test metodu ile gecerli bi şehir adı verildiginde appin dogru sekilde calısıp calısmadıgı
    test ettim.
    """
    def test_valid_city(self):
        response = self.client.post('/', data={'city': 'Mexico'})
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('Türkçe karakter kullanmayınız', response.data.decode('utf-8'))
        self.assertIn('Mexico', response.data.decode('utf-8'))

    """
    bu metotta varsayılan sehir adıyla (istanbul) '/' urline yapılan GET istegi sonucunda appin dogru 
    calısıp calısmadıgın testidir. 
    şimdi assertEqual ile 200 varmı yokmu testi yaptık. assertNotIn ile türkçe karakter kullanmayınız
    metinin bulunmadıgını dogruladık. assertIn ile yanıt içindeki metnin (istanbul) bulunup bulumadıgına 
    baktık sorun yok ise test basarılıdır
    
    """
    def test_default_city(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('Türkçe karakter kullanmayınız', response.data.decode('utf-8'))
        self.assertIn('Istanbul', response.data.decode('utf-8'))
"""
burda test sınıfının calıstırılmasını sagladım.
"""
if __name__ == '__main__':
    unittest.main()
