from django.urls import path
from .views import EmployeeProfileViewSet
from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


router = DefaultRouter()
router.register('employees', EmployeeProfileViewSet, basename="employees")
urlpatterns = router.urls