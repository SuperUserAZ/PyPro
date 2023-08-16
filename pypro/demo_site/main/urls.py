from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import about, signup, login, profile

urlpatterns = [
    path('', login, name="registration"),
    path('about/', about, name="about"),
    path('authorization/', signup, name="authorization"),
    path('profile/', profile, name='profile')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
