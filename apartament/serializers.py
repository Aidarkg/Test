from rest_framework import serializers
from apartament.models import Apartment, ObjectApartament


class ObjectApartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectApartament
        fields = '__all__'


class ApartmentSerializer(serializers.ModelSerializer):
    # apartament_object = serializers.StringRelatedField()
    # status = serializers.SerializerMethodField()

    class Meta:
        model = Apartment
        fields = '__all__'

    # def get_apartament_object(self, obj):
    #     return obj.apartament_object.name

    # def get_status(self, obj):
    #     return obj.get_status_display()
    