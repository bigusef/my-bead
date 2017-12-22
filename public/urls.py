from django.conf.urls import url
from .views import HomeView, MattressView, ProductView, ContactUsView, AboutUsView, ManufacturerView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^mattress/(?P<pk>\d+)/$', MattressView.as_view(), name='mattress'),
    url(r'^product/(?P<pk>\d+)/$', ProductView.as_view(), name='product'),
    url(r'^Manufacturer/$', ManufacturerView.as_view(), name='manufacturer'),
    url(r'^contact-us/$', ContactUsView.as_view(), name='contact'),
    url(r'^about-us/$', AboutUsView.as_view(), name='about'),
]
