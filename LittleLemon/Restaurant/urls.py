from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet

router = DefaultRouter()
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/items', views.MenuItemView.as_view(), name='menu-items'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
    path('api/', include(router.urls)),
]
