from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet)
router.register(r'quote', views.QuoteViewSet)
router.register(r'policies', views.PolicyViewSet)

# Allowed URL patterns
urlpatterns = [
    path('api/v1/create_customer/', views.CustomerCreate.as_view()),
    path('api/v1/', include(router.urls)),
]