from django.urls import path, re_path
from .views import *

app_name = 'ekonomi'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('headline_berita/', BeritaHeadlineView.as_view(), name='headline_berita'),
    path('get_headline_berita/', get_headline_berita, name='get_headline_berita'),

    path('everything_berita/', BeritaEverythingView.as_view(), name='everything_berita'),
    path('get_everything_berita/', get_everything_berita, name='get_everything_berita'),


    # path('notifications/', NotificationListView.as_view(), name='notifications'),
    # re_path('mark-as-read/(?P<slug>\d+)/$', mark_as_read, name='mark_as_read'),

]
