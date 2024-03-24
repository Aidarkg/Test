from django.urls import path
from manager.views import ManagerListAPIView, ManagerUpdateDeleteAPIView, LoginAPIView, LogoutAPIView


urlpatterns = [
    path('api/v1/manager/', ManagerListAPIView.as_view(), name='manager'),
    path('api/v1/manager/<int:id>/', ManagerUpdateDeleteAPIView.as_view(), name='manager_detail'),
    path('api/v1/login/', LoginAPIView.as_view(), name='login'),
    path('api/v1/logout/', LogoutAPIView.as_view(), name='logout'),
]
