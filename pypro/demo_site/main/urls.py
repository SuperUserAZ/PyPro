from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, about, signup, login

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('registration/', signup, name="registration"), 
    path('authorization/', login, name="authorization"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)