from django.test import TestCase, SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):

    def test_home_page_view_status_code(self):
        request = self.client.get('/')
        self.assertEqual(request.status_code, 200)


    def test_about_page_view_code(self):

        request = self.client.get('/about/')
        self.assertEqual(request.status_code, 200)