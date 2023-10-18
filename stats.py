from collections import Counter

from helpers import ngrams
from config import STOP_WORDS, UNWANTED_CHARS


def sanitize_article(article: str, unwanted_chars=UNWANTED_CHARS):
    for c in unwanted_chars:
        article = article.replace(c, "")
    return article.lower()


def count_words(text: str):
    return len(text.split())


def count_letters(text: str):
    return sum(1 for c in text if c.isalpha())


def keywords_extraction(text: str, num_of_keys: int):
    sanitized_article = sanitize_article(text)
    words = [w for w in sanitized_article.split() if w not in STOP_WORDS]
    counts = words
    for n_count in [2, 3]:
        for x in ngrams(words, n_count):
            counts.append(" ".join(x))
    counts = Counter(counts)
    return list(map(lambda tup: tup[0], counts.most_common(num_of_keys)))
