from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ChatRoomViewSet, MessageViewSet,LoginApiview

router = DefaultRouter()
router.register(r'chatrooms', ChatRoomViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('',views.home),
    path('api/', include(router.urls)),
     path('api/login/', LoginApiview.as_view(), name='login'),
]