from itertools import tee


def ngrams(sequence, n: int):
    """
    Simplified https://tedboy.github.io/nlps/generated/generated/nltk.ngrams.html.
    Return n-length ngrams generated from sequence in the iterable.

    ngrams(range(6), 2) --> [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
    ngrams(range(6), 3) --> [(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 5)]
    """
    iterables = tee(sequence, n)
    for i, sub_iterable in enumerate(iterables):
        for _ in range(i):
            next(sub_iterable, None)
    return list(zip(*iterables))
