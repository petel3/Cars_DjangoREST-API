from django.urls import path

from DjangoRestProject.cars_api.views import BrandListCreate, BrandGetUpdateDelete, UserList, UserGetUpdateDelete, \
    UserCreate, ModelListCreate, ModelGetUpdateDelete, UserCarListCreate, UserCarGetUpdateDelete

urlpatterns = [
    path('users/register', UserCreate.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:user_id>', UserGetUpdateDelete.as_view()),
    path('brands/', BrandListCreate.as_view()),
    path('brands/<int:brand_id>', BrandGetUpdateDelete.as_view()),
    path('models/', ModelListCreate.as_view()),
    path('models/<int:model_id>', ModelGetUpdateDelete.as_view()),
    path('usercar/', UserCarListCreate.as_view()),
    path('usercar/<int:user_car_id>', UserCarGetUpdateDelete.as_view()),
]
