from django.contrib import admin
from .models import Booking, Menu, MenuItem

# Register your models here.
admin.site.register(Booking)
admin.site.register(MenuItem)

admin.site.register(Menu)