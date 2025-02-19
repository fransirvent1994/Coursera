from django.test import TestCase
from .models import Menu, Booking

class MenuViewTestCase(TestCase):
    def test_create_menu_item(self):
        item = Menu.objects.create(name="Pizza", price=12.99)
        self.assertEqual(item.name, "Pizza")

class BookingTestCase(TestCase):
    def test_create_booking(self):
        booking = Booking.objects.create(name="John Doe", date="2025-02-20")
        self.assertEqual(booking.name, "John Doe")
