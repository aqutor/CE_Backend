"""CE_Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('eva.urls')),
]

# Add URL maps to redirect the base URL to API application
# Clear browser cache if this configuration won't work
urlpatterns += [
    path('', RedirectView.as_view(url='api/', permanent=True)),
]

# Set static file path
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Set admin site information
admin.site.site_header = "Calligraphy Evaluation Content Administration"
admin.site.site_title = "Calligraphy Evaluation Content Administration"
admin.site.index_title = "Calligraphy Evaluation Content Administration"
