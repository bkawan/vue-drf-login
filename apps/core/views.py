# Create your views here.


from django.views.generic import TemplateView


class LandingPageTemplateView(TemplateView):
    template_name = 'core/landing.html'
