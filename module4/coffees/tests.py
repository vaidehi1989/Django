from django.urls import reverse
from .models import Coffee
from django.test import TestCase


# Value getting inserted into database correctly.
# class CoffeeModelTest(TestCase):
#
#     def setUp(self):
#         Coffee.objects.create(name='TestCoffee', flavour='abc', roast='xyz', processing='pqr', description='qwerty',
#                               price=80)
#
#     def test_coffee_content(self):
#         ic = Coffee.objects.get(id=1)
#         self.assertEqual(ic.name, 'TestCoffee')
#         self.assertEqual(ic.flavour, 'abc')
#         self.assertEqual(ic.price, 80)


class HomePageViewTest(TestCase):

    def setUp(self):
        Coffee.objects.create(name='TestCoffee', flavour='abc', roast='xyz', processing='pqr', description='qwerty',
                              price=80)

    def test_coffee_list_view(self):
        response = self.client.get(reverse('listcoffees')) # Reverse calling
        # response = self.client.get('/coffees/')  # Forward Calling

        # Checks if url - /coffees/ is working correct
        self.assertEqual(response.status_code, 200)

        # Checks if template - listcoffees.html is getting fetched correctly
        self.assertTemplateUsed(response, 'listcoffees.html')

        # Checks if content on the template is displayed correctly.
        self.assertContains(response, 'TestCoffee')
