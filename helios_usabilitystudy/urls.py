"""helios_usabilitystudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from helios_usabilitystudy import views
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + [
    url(r'^admin/', admin.site.urls),
    url(r'^login$', views.login, name='login'),
    # url(r'^logout$', views.logout, name='logout'),
    url(r'^main/', include('helios_main.urls')),
    url(r'^institute/', include('helios_institutes.urls')),
    url(r'^smartphone/', include('helios_smartphone.urls')),
    url(r'^save$', views.save_timestamp, name='save_timestamp'),
    url(r'^.*', views.welcome, name='welcome_DE')
]
