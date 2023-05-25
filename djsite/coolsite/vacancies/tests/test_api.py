from rest_framework.test import APITestCase

class VacanciesTestCase(APITestCase):
    def test_get(self):
        url = 'http://127.0.0.1:8000/'
        print(url)
        response = self.client.get(url)
        print(response)
