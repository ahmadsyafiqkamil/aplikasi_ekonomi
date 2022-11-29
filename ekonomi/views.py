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
import requests
import pandas as pd
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


class BeritaHeadlineView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'content/headline_berita.html'


class BeritaEverythingView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'content/everything_berita.html'


def get_headline_berita(request):
    if request.method == 'POST':
        query = "" if request.POST["search_form"] == "" else request.POST["search_form"]
        qintitle = "" if request.POST["search_form"] == "" else request.POST["search_form"]
        country = "id" if request.POST["country"] == "1" else "us"
        data = api.get_top_headlines(q=query, qintitle=qintitle, country=country, page_size=100)

        df = pd.DataFrame.from_dict(data["articles"])
        print(df["description"])
        return JsonResponse(data)


def get_everything_berita(request):
    if request.method == 'POST':
        query = "" if request.POST["search_form"] == "" else request.POST["search_form"]
        qintitle = "" if request.POST["search_form"] == "" else request.POST["search_form"]
        data = api.get_everything(q=query, qintitle=qintitle, page_size=100)
        df = pd.DataFrame.from_dict(data["articles"])
        print(df["description"])
        return JsonResponse(data)
