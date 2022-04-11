
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apis.urls')),
    path('api-auth/', include('rest_framework.urls')),
    
    
    
]
