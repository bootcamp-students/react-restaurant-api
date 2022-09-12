from django.urls import path, include
from rest_framework import routers
from menu_items.views import CategoryViewSet, ItemViewSet, index, send_json

router = routers.DefaultRouter()

router.register(r'category', CategoryViewSet)
router.register(r'json', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
