from django.contrib import admin
from cars.models import Car, UserProfile, Wishlist, TestDrive, Dealer


# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'manufacturer', 'price', 'mileage', ]


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'DOB', ]


class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'car']

class TestDriveAdmin(admin.ModelAdmin):
    list_display = ['user', 'car']


class DealerAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_profile']


admin.site.register(Car, CarAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(TestDrive, TestDriveAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Dealer, DealerAdmin)
