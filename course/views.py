from django.views.generic import (TemplateView)


class HomeView(TemplateView):
    template_name = 'components/home.html'


class AboutView(TemplateView):
    template_name = 'components/about.html'


class ServicesView(TemplateView):
    template_name = 'components/service.html'