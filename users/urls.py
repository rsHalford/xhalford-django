#from django.conf import settings
#from django.contrib.auth.views import logout
from django.urls import include, path
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('settings/', views.AccountSettings, name='settings'),
    path('register/', views.register, name='register'),
]
#path('oauth/', include('social_django.urls')),
#path('oauth/', include('social.apps.django_app.urls')),
#path('logout/', views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
