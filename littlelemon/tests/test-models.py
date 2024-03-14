from django.test import TestCase
from restaurant import models

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = models.Menu.objects.create(title="Ice Cream", price = 80, inventory = 100)
        self.assertEqual(item, "Ice Cream : 80 ")
