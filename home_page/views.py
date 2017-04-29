from django.http import HttpResponse
from django.views.generic import TemplateView


def index(request):
    return HttpResponse("Hello, world")


class HomePage(TemplateView):
    template_name = 'base.html'
