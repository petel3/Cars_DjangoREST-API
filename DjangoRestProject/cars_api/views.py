from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from DjangoRestProject.cars_api.models import CarBrand, User, CarModel, UserCar
from DjangoRestProject.cars_api.serializers import BrandSerializer, UserSerializer, UserRegisterSerializer, \
    ModelSerializer, UserCarSerializer

"""
class UserCreate in API
http://127.0.0.1:8000/cars/users/register
Use this link to register a new user.
"""

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)

"""
class UserList in API
http://127.0.0.1:8000/cars/users
Use this link to read data for users.
"""

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


"""
class UserGetUpdateDelete in API
http://127.0.0.1:8000/cars/users/user_id
Use this link with user_id to read data for current user to delete it and update his data.
"""

class UserGetUpdateDelete(APIView):
    def put(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

"""
class BrandListCreate in API
http://127.0.0.1:8000/cars/brands
Use this link to read and post data for car brands.
"""

class BrandListCreate(APIView):
    def get(self, request):
        cars = CarBrand.objects.all()
        serializer = BrandSerializer(cars, many=True)

        return Response(serializer.data)

    def post(self, request):
        brand_serializer = BrandSerializer(data=request.data)
        if brand_serializer.is_valid():
            brand_serializer.save()
            return Response(brand_serializer.data, status=status.HTTP_201_CREATED)
        return Response(brand_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
class BrandGetUpdateDelete in API
http://127.0.0.1:8000/cars/brands/brand_id
Use this link with brand_id to read data for current brand to delete it or update the current brand data.
"""

class BrandGetUpdateDelete(APIView):
    def put(self, request, brand_id):
        try:
            brand = CarBrand.objects.get(id=brand_id)
            serializer = BrandSerializer(brand, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, brand_id):
        try:
            brand = CarBrand.objects.get(id=brand_id)
            brand_serializer = BrandSerializer(brand)
            return Response(brand_serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, brand_id):
        try:
            brand = CarBrand.objects.get(id=brand_id)
            brand.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

"""
class ModelListCreate in API
http://127.0.0.1:8000/cars/models/
Use this link to read and post data for car models.
"""

class ModelListCreate(APIView):
    def get(self, request):
        cars = CarModel.objects.all()
        serializer = ModelSerializer(cars, many=True)

        return Response(serializer.data)

    def post(self, request):
        model_serializer = ModelSerializer(data=request.data)
        if model_serializer.is_valid():
            model_serializer.save()
            return Response(model_serializer.data, status=status.HTTP_201_CREATED)
        return Response(model_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
class ModelGetUpdateDelete in API
http://127.0.0.1:8000/cars/models/model_id
Use this link with model_id to read data for current model to delete it or update the current model data.
"""

class ModelGetUpdateDelete(APIView):
    def put(self, request, model_id):
        try:
            model = CarModel.objects.get(id=model_id)
            serializer = ModelSerializer(model, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, model_id):
        try:
            model = CarModel.objects.get(id=model_id)
            model_serializer = ModelSerializer(model)
            return Response(model_serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, model_id):
        try:
            model = CarModel.objects.get(id=model_id)
            model.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

"""
class UserCarListCreate in API
http://127.0.0.1:8000/cars/usercar/
Use this link to read and post data for UserCar.
"""

class UserCarListCreate(APIView):
    def get(self, request):
        user_car = UserCar.objects.all()
        serializer = UserCarSerializer(user_car, many=True)

        return Response(serializer.data)

    def post(self, request):
        user_car_serializer = UserCarSerializer(data=request.data)
        if user_car_serializer.is_valid():
            user_car_serializer.save()
            return Response(user_car_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_car_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
class UserCarGetUpdateDelete in API
http://127.0.0.1:8000/cars/usercar/user_car_id
Use this link with user_car_id to read data for current user_car to delete it or update the current user_car data.
"""

class UserCarGetUpdateDelete(APIView):
    def put(self, request, user_car_id):
        try:
            user_car = UserCar.objects.get(id=user_car_id)
            serializer = UserCarSerializer(user_car, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, user_car_id):
        try:
            user_car = UserCar.objects.get(id=user_car_id)
            user_car_serializer = UserCarSerializer(user_car)
            return Response(user_car_serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, user_car_id):
        try:
            user_car = UserCar.objects.get(id=user_car_id)
            user_car.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
