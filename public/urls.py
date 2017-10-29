from django.conf.urls import url
from .views import index, ContactUsView, AboutUsView

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^contact-us/$', ContactUsView.as_view(), name='contact'),
    url(r'^about-us/$', AboutUsView.as_view(), name='about'),
]
