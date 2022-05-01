from django.contrib import admin

from DjangoRestProject.cars_api.models import CarBrand, User, CarModel, UserCar

admin.site.register(CarBrand)
admin.site.register(User)
admin.site.register(CarModel)
admin.site.register(UserCar)
