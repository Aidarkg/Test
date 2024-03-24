from django.shortcuts import render
from apartament.models import Apartment, ObjectApartament
from apartament.serializers import ApartmentSerializer, ObjectApartamentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination



class ApartamentListAPIView(ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    pagination_class = PageNumberPagination
    filterset_fields = ['name']


class ApartamentUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    lookup_field = 'id'


class ObjectApartamentListAPIView(ListCreateAPIView):
    queryset = ObjectApartament.objects.all()
    serializer_class = ObjectApartamentSerializer


class ObjectApartamentUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ObjectApartament.objects.all()
    serializer_class = ObjectApartamentSerializer
    lookup_field = 'id'
