import argparse

from unit_tests import perform_tests
from config import (
    AVAILABLE_BLOGS,
    NUM_OF_ARTICLES,
)
from statistics import (
    count_words,
    count_letters,
    keywords_extraction,
)
from parsing import (
    parse_article,
    get_latest_urls,
)


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
