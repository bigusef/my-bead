from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^', include('public.urls', namespace='Public')),
    url(r'^admin/', admin.site.urls),
    url(r'^atum/$', RedirectView.as_view(url='http://atumlab.com/'), name='ATUMlab')
]

