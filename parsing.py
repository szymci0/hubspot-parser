import requests
from bs4 import BeautifulSoup
from config import HUBSPOT_URL


def parse_page(url: str):
    res = requests.get(url)
    return BeautifulSoup(res.text, "html.parser")


def get_latest_urls(blog: str):
    url = HUBSPOT_URL + blog
    res_html = parse_page(url)
    latest = res_html.find("div", class_="blog-latest-articles-content")
    latest_articles_urls = []
    for post in latest.find_all("li", class_="blog-post-list-item"):
        latest_articles_urls.append(post.find('a')['href'])
    return latest_articles_urls


def parse_article(article_url: str):
    article_html = parse_page(article_url)
    return article_html.find("div", "hsg-rich-text__wrapper").get_text()
