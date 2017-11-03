from django.views.generic import TemplateView, DetailView

from django.shortcuts import get_object_or_404
from .models import CompanyInfo, Mattress, Products


class HomeView(TemplateView):
    template_name = 'home.html'


class MattressView(DetailView):
    template_name = 'detail-item.html'
    model = Mattress


class ProductView(DetailView):
    template_name = 'detail-item.html'
    model = Products


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
        info = get_object_or_404(CompanyInfo, pk=1)
        context['word'] = info.about_word
        return context

