from django.urls import path


from rest_framework.routers import DefaultRouter

from src.apps.product import views

router = DefaultRouter()

router.register("product", views.ProductViewSet, basename="product")
router.register('category/', views.CategoryViewSrt,  basename="category")


urlpatterns = []



urlpatterns += router.urls