from django.urls import path
from app.views import LoginAPIView  


urlpatterns = [
    path("api/login/", LoginAPIView.as_view(), name="login_user"),
]