from django.urls import path, re_path
from .views import *

app_name = 'ekonomi'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('berita/', BeritaView.as_view(), name='berita'),
    path('get_berita/', get_berita, name='get_berita'),

    # path('notifications/', NotificationListView.as_view(), name='notifications'),
    # re_path('mark-as-read/(?P<slug>\d+)/$', mark_as_read, name='mark_as_read'),

]
