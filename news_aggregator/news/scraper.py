from .models import HeadLine



def scrape_wired(soup, url):
    """Функция для парсинга статей с сайта wired.com"""
    for tag in soup.find_all("div", {"class": "card-component"}):
        try:
            tag_header = tag.find("li", {"class": "card-component__description"})

            article_title = tag_header.find("h2").get_text().strip()
            article_href = url + tag_header.find_all("a")[0]['href']
            article_img = tag.find("div", {"class": "image-group-component"}).find("img")["src"]

            new_headline = HeadLine()
            if not HeadLine.objects.filter(title=article_title):
                new_headline.title = article_title
                new_headline.url = article_href
                new_headline.image = article_img
                new_headline.save()
        except:
            continue


def scrape_nytimes(soup, url):
    """Функция для парсинга статей с сайта nytimes.com"""
    for tag in soup.find_all("li", {"class": "ekkqrpp3"}):
        try:
            tag_header = tag.find("h2", {"class": "css-y3otqb e134j7ei0"})

            article_title = tag_header.get_text().strip()
            article_href = 'https://www.nytimes.com' + tag_header.find("a")["href"]
            article_img = tag.find("figure", {"class": "photo"}).find("img")["src"]

            new_headline = HeadLine()
            if not HeadLine.objects.filter(title=article_title):
                new_headline.title = article_title
                new_headline.url = article_href
                new_headline.image = article_img
                new_headline.save()
        except:
            continue


def scrape_pitchfork(soup, url):
    """Функция для парсинга статей с сайта pitchfork.com"""
    for tag in soup.find_all("div", {"class": "module"}):
        try:
            tag_header = tag.find("a", {"class": "title-link"})
            article_title = tag_header.get_text().strip()
            article_href = 'https://pitchfork.com' + tag_header['href']
            article_img = tag.find("div", {"class": "image"}).find("img")["src"]

            new_headline = HeadLine()
            if not HeadLine.objects.filter(title=article_title):
                new_headline.title = article_title
                new_headline.url = article_href
                new_headline.image = article_img
                new_headline.save()
        except:
            continue