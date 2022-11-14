from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from notifications.utils import slug2id
from django.http import JsonResponse
import os
from dotenv import load_dotenv
from newsapi import NewsApiClient
import json

load_dotenv()

news_keys = os.getenv('NEWS_KEY')
fred_keys = os.getenv('FRED_API_KEY')
api = NewsApiClient(api_key=news_keys)


# Create your views here.

class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'content/home.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    success_url = '/'


class BeritaView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'content/berita.html'


def get_berita(request):
    if request.method == 'POST':
        print(request.POST)
        data = api.get_everything(q=request.POST["search_form"])
        print(data)
        return JsonResponse(data)
