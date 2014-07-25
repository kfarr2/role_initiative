from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
	
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
