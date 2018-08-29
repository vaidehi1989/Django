# from django.urls import reverse
# from .models import Icecream
# from django.test import TestCase
#
#
# # Value getting inserted into database correctly.
# class IcecreamModelTest(TestCase):
#
#     def setUp(self):
#         Icecream.objects.create(name='TestCream', category="candy", price=80)
#
#     def test_icecream_content(self):
#         ic = Icecream.objects.get(id=1)
#         self.assertEqual(ic.name, 'TestCream')
#         self.assertEqual(ic.category, 'candy')
#         self.assertEqual(ic.price, 80)
#
#
# class HomePageViewTest(TestCase):
#
#     def setUp(self):
#         Icecream.objects.create(name='TestCream2', category="candy", price=80)
#
#     def test_icecream_list_view(self):
#         # response = self.client.get(reverse('listicreams')) # Reverse calling
#         response = self.client.get('/icecreams/')  # Forward Calling
#
#         # Checks if url - /icecreams/ is working correct
#         self.assertEqual(response.status_code, 200)
#
#         # Checks if template - listicreams.html is getting fetched correctly
#         self.assertTemplateUsed(response, 'listicreams.html')
#
#         # Checks if content on the template is displayed correctly.
#         self.assertContains(response, 80)
