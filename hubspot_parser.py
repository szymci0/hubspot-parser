import requests
import argparse
from itertools import tee
from collections import Counter
from bs4 import BeautifulSoup

from unit_tests import perform_tests
from config import (
    HUBSPOT_URL,
    AVAILABLE_BLOGS,
    NUM_OF_ARTICLES,
    UNWANTED_CHARS,
    STOP_WORDS,
)


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


def count_words(text: str):
    return len(text.split())


def count_letters(text: str):
    return sum(1 for c in text if c.isalpha())


def sanitize_article(article: str, unwanted_chars=UNWANTED_CHARS):
    for c in unwanted_chars:
        article = article.replace(c, "")
    return article.lower()


def ngrams(sequence, n):
    iterables = tee(sequence, n)
    for i, sub_iterable in enumerate(iterables):
        for _ in range(i):
            next(sub_iterable, None)
    return zip(*iterables)


def keywords_extraction(text: str, num_of_keys: int):
    sanitized_article = sanitize_article(text)
    words = [w for w in sanitized_article.split() if w not in STOP_WORDS]
    counts = words
    for n_count in [2, 3]:
        for x in list(ngrams(words, n_count)):
            counts.append(" ".join(x))
    counts = Counter(counts)
    return list(map(lambda tup: tup[0], counts.most_common(num_of_keys)))


def parse_hubspot(
    blog: str,
    num_of_keys: int,
    test=False
):
    if test:
        perform_tests()
        return

    if blog not in AVAILABLE_BLOGS:
        print(f"Blog argument must be one of {AVAILABLE_BLOGS}")
        return

    urls = get_latest_urls(blog)
    if len(urls) < NUM_OF_ARTICLES:
        print("Failed to fetch latest articles urls!")
        return

    for idx in range(NUM_OF_ARTICLES):
        article = parse_article(urls[idx])
        print(f"{idx + 1}. article:")
        print(f"Number of words: {count_words(article)}")
        print(f"Number of letters: {count_letters(article)}")
        print(f"Most used keywords: {keywords_extraction(article, num_of_keys=num_of_keys)}")


if __name__ == '__main__':
    arguments = argparse.ArgumentParser(
        description="Script for parsing 3 latest posts from chosen HubSpot blog"
    )
    arguments.add_argument(
        "-b", "--blog",
        default="marketing",
        help=f"One of {AVAILABLE_BLOGS}",
        type=str
    )
    arguments.add_argument(
        "-t", "--test",
        help="Perform unit tests",
        action="store_true"
    )
    arguments.add_argument(
        "-k", "--keywords",
        default=5,
        help=f"Number of keywords",
        type=int
    )
    args = arguments.parse_args()

    parse_hubspot(
        args.blog,
        test=args.test,
        num_of_keys=args.keywords,
    )
