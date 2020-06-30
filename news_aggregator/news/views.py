import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from .models import HeadLine

from . import scraper
from .models import HeadLine


requests.packages.urllib3.disable_warnings()


def scrape(request):
    """Фнкция для парсинга статей с сайтов"""
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    # получаем ссылку на WIRED.COM и собираем оттуда статьи
    url_wired = "https://www.wired.com"

    content = session.get(url_wired).content
    soup_wired = BeautifulSoup(content, "html.parser")

    scraper.scrape_wired(soup_wired, url_wired)

    # получаем ссылку на NYTIMES.COM и собираем оттуда статьи
    url_nytimes = "https://www.nytimes.com/section/world"

    content = session.get(url_nytimes).content
    soup_nytimes = BeautifulSoup(content, "html.parser")

    scraper.scrape_nytimes(soup_nytimes, url_nytimes)

    # получаем ссылку на PITCHFORK.COM и собираем оттуда статьи
    url_pitchfork = "https://pitchfork.com/news"

    content = session.get(url_pitchfork).content
    soup_pitchfork = BeautifulSoup(content, "html.parser")

    scraper.scrape_pitchfork(soup_pitchfork, url_pitchfork)
    
    return redirect("../")


def news_list(request):
    headlines = HeadLine.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, 'news/home.html', context)
