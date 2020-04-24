from django.test import TestCase, SimpleTestCase
from django.urls import reverse
# Create your tests here.

# class SimpleTests(SimpleTestCase):

#     def test_home_page_view_status_code(self):
#         request = self.client.get('/')
#         self.assertEqual(request.status_code, 200)


#     def test_about_page_view_code(self):

#         request = self.client.get('/about/')
#         self.assertEqual(request.status_code, 200)

class HomePageTest(TestCase):

    def test_view_url_exists_at_proper_location(self):
        request = self.client.get('/')
        self.assertEqual(request.status_code, 200)

    def test_view_url_by_name(self):
        request = self.client.get(reverse('home'))
        self.assertEqual(request.status_code, 200)

    def test_view_uses_correct_template(self):
        request = self.client.get(reverse('home'))
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'home.html')

class AboutPageTest(TestCase):

    def test_view_url_exists_at_proper_location(self):
        request = self.client.get('/about/')
        self.assertEqual(request.status_code, 200)

    def test_view_url_by_name(self):
        request = self.client.get(reverse('about'))
        self.assertEqual(request.status_code, 200)

    def test_view_uses_correct_template(self):
        request = self.client.get(reverse('about'))
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'about.html')
