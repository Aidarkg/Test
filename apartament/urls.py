from django.urls import path
from apartament.views import ApartamentListAPIView, ApartamentUpdateDeleteAPIView, \
    ObjectApartamentListAPIView, ObjectApartamentUpdateDeleteAPIView, apartamentlistview


urlpatterns = [
    path('api/v1/apartament/', ApartamentListAPIView.as_view(), name='apartaments'),
    path('api/v1/apartament/<int:id>/', ApartamentUpdateDeleteAPIView.as_view(), name='apartament_detail'),
    path('api/v1/object/', ObjectApartamentListAPIView.as_view(), name='objectl'),
    path('api/v1/object/<int:id>/', ObjectApartamentUpdateDeleteAPIView.as_view(), name='object_detail'),
    path('apartament/', apartamentlistview)
]