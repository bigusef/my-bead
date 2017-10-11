from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^', include('public.urls', namespace='Public')),
    url(r'^admin/', admin.site.urls),
    url(r'^atum/$', RedirectView.as_view(url='http://atumlab.com/'), name='ATUMlab')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

