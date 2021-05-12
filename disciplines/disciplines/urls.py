from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('mainapp.api.urls')),
    path('', include('mainapp.urls')),
    path('user/token/', obtain_auth_token, name='get_token'),
]
