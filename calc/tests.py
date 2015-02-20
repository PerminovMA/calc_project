from django.test import TestCase
from django.test.client import Client
from calc.calc_logic import ERROR_STRING

client = Client()


class TestCalc(TestCase):

    def test1(self):
        response1 = client.post('/calc/', {'display_field': '-11+11'}).content
        response2 = client.post('/calc/', {'display_field': '5+2+5-4+7-6+11'}).content
        response3 = client.post('/calc/', {'display_field': '11++11'}).content
        response4 = client.post('/calc/', {'display_field': '11+11-'}).content
        self.assertEqual((response1, response2, response3, response4), ('0', '20', ERROR_STRING, ERROR_STRING))

    def test2(self):
        response1 = client.post('/calc/', {'display_field': '1,1+0,9'}).content
        response2 = client.post('/calc/', {'display_field': '42,5+12312323432,7'}).content
        response3 = client.post('/calc/', {'display_field': '1111'}).content
        response4 = client.post('/calc/', {'display_field': '11,11,11'}).content
        self.assertEqual((response1, response2, response3, response4), ('2', '12312323475,2', '1111', ERROR_STRING))

    def test3(self):
        response1 = client.post('/calc/', {'display_field': ''}).content
        response2 = client.post('/calc/', {'display_field': ',5'}).content
        response3 = client.post('/calc/', {'display_field': '123*321/234,6'}).content
        response4 = client.post('/calc/', {'display_field': '5/0'}).content
        self.assertEqual((response1, response2, response3, response4), ('', '0,5', '168,299232737', ERROR_STRING))

    def test4(self):
        response1 = client.post('/calc/', {'display_field': '5/2+0,5'}).content
        response2 = client.post('/calc/', {'display_field': '5.0'}).content
        response3 = client.post('/calc/', {'display_field': '43**54'}).content
        response4 = client.post('/calc/', {'display_field': '4*5+2-45*4,2+63,2/12*54,2/2/2/2/2/2/2/2/2/2'}).content
        self.assertEqual((response1, response2, response3, response4), ('3', '5', ERROR_STRING, '-166,442473958'))

    def test5(self):
        response1 = client.post('/calc/', {'display_field': '1/11111111111'}).content
        response2 = client.post('/calc/', {'display_field': '9,00000000009e-11+1'}).content
        self.assertEqual((response1, response2), ('9,00000000009e-11', '1,00000000009'))