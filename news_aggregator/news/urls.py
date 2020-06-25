from django.urls import path
from .views import scrape_wired, news_list

urlpatterns = [
    path('scrape_wired', scrape_wired, name='scrape_wired'),
    path('', news_list, name='home'),
]
