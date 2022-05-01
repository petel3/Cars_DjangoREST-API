from rest_framework import serializers
from DjangoRestProject.cars_api.models import CarBrand, User, CarModel, UserCar


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = "__all__"


class ModelSerializer(serializers.ModelSerializer):
    car_brand = serializers.StringRelatedField()

    class Meta:
        model = CarModel
        fields = "__all__"


class UserCarSerializer(serializers.ModelSerializer):
    user_key = serializers.StringRelatedField()
    car_brand = serializers.StringRelatedField()
    car_model = serializers.StringRelatedField()

    class Meta:
        model = UserCar
        fields = "__all__"
