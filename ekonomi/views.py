from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from notifications.utils import slug2id


# Create your views here.

class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'content/home.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    success_url = '/'


class BeritaView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'content/berita.html'
