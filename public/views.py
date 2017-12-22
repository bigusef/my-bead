from django.views.generic import TemplateView, DetailView

from django.shortcuts import get_object_or_404
from .models import CompanyInfo, Mattress, Products, Manufacturer


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        try:
            context['bubbly'] = Mattress.objects.get(name='بابلي')
            context['mattress_list'] = Mattress.objects.filter(is_new__exact=True).exclude(name="بابلي")[:2]
            context['product_list'] = Products.objects.filter(is_new__exact=True)
        except Mattress.DoesNotExist:
            pass
        return context


class MattressView(DetailView):
    template_name = 'detail-item.html'
    model = Mattress

    def get_context_data(self, **kwargs):

        context = super(MattressView, self).get_context_data(**kwargs)
        context['object_list'] = Mattress.objects.all()
        return context


class ProductView(DetailView):
    template_name = 'detail-item.html'
    model = Products

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['object_list'] = Products.objects.all()
        return context


class ManufacturerView(TemplateView):
    template_name = 'manufacturer.html'

    def get_context_data(self, **kwargs):
        context = super(ManufacturerView, self).get_context_data(**kwargs)
        context['list'] = Manufacturer.objects.all()
        return context


class ContactUsView(TemplateView):
    template_name = 'contact-us.html'

    def get_context_data(self, **kwargs):
        context = super(ContactUsView, self).get_context_data(**kwargs)
        info = get_object_or_404(CompanyInfo, pk=1)
        context['phone'] = info.telephones.all()
        context['email'] = info.emails.all()
        context['address'] = info.addresses.all()
        return context


class AboutUsView(TemplateView):
    template_name = 'about-us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)

        info = CompanyInfo.objects.first()
        if info:
            context['word'] = info.about_word
        return context

