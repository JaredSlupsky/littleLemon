from django.test import TestCase
from restaurant import views, models

class MenuViewTest(TestCase):
    def setUp(self):
        item = models.Menu.objects.create(title="Ice Cream", price = 80, inventory = 100)

 
