from django.urls import path, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('account.urls')),
    path('', include('ui.urls')),
    # path('/login', include('ui.urls'))
]
