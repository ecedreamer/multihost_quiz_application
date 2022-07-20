from website.utils import server_sent_event
from .views import HomeView, LoginView, RegisterView, LogoutView
from django.urls import path

app_name = "website"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login", LoginView.as_view(), name="login"),
    path("register", RegisterView.as_view(), name="register"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("sse/", server_sent_event, name="sse")
]