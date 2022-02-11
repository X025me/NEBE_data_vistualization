from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from data_v.views import catchall
from api.user.viewsets import VerifyEmail

from django.conf.urls.static import static

urlpatterns = [
    path('', catchall),
    path('admin/', admin.site.urls),
    path("api/users/", include(("api.routers", "api"), namespace="api")),
    path("data/read/", include("data_v.urls")),
    path('data/requests/', include('interaction.urls')),
    path("verify/", VerifyEmail.as_view(), name="email-verify")
]
