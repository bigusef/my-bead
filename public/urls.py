from django.conf.urls import url
from .views import index, contact_us

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^contact-us/$', contact_us, name='contact'),
]
