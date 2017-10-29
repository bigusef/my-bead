from django.views.generic import TemplateView

from django.shortcuts import render, get_object_or_404
from .models import CompanyInfo


def index(request):
    return render(request, 'home.html', {})


class ContactUsView(TemplateView):
    template_name = 'contact-us.html'

    def get_context_data(self, **kwargs):
        context = super(ContactUsView, self).get_context_data(**kwargs)
        info = get_object_or_404(CompanyInfo, pk=1)
        context['phone'] = info.telephones.all()
        context['email'] = info.emails.all()
        context['adress'] = info.adresses.all()
        return context


class AboutUsView(TemplateView):
    template_name = 'about-us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        info = get_object_or_404(CompanyInfo, pk=1)
        context['word'] = info.about_word
        return context

