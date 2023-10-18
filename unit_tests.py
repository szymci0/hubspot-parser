from stats import (
    count_words,
    count_letters,
    keywords_extraction,
)
from helpers import ngrams

TEST_TEXT1 = """
    Paste your text here or start fresh. Duplicates are highlighted in real-time. (Once you begin, these instructions will be cleared.)

The list of duplicates can be found next to the editor. You can toggle highlighting for individual words by clicking on them.

The toolbar offers several controls. Use the first two buttons for undoing and redoing edits. Adjust the minimum word length and minimum number of repeats using the sliders (third and fourth buttons on smaller screens). The word and character counts are displayed on the right side.

When you're ready, you can copy your text with the "Copy All" button next to the top-right menu. Use the menu for additional options, such as selecting your preferred theme: light, dark, or system.
"""

TEST_TEXT2 = "Test, testing,   'test'... Lorem  ipsum"
TEST_TEXT3 = """lorem ipsum dolor sit amet, lorem ipsum dolor sit amet, Lorem ipsum dolor sit amet, sit amet.  Neque
             porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non
             numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. """


def count_letters_test():
    result = count_letters(TEST_TEXT1)
    assert result == 591
    result = count_letters(TEST_TEXT2)
    assert result == 25
    result = count_letters(TEST_TEXT3)
    assert result == 235


def count_words_test():
    result = count_words(TEST_TEXT1)
    assert result == 122
    result = count_words(TEST_TEXT2)
    assert result == 5
    result = count_words(TEST_TEXT3)
    assert result == 47


def ngrams_test():
    result = ngrams(range(8), 3)
    assert result == [(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6), (5, 6, 7)]
    result = ngrams(range(6), 2)
    assert result == [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
    result = ngrams(range(1), 2)
    assert result == []


def keywords_extraction_test():
    result = keywords_extraction(TEST_TEXT1, num_of_keys=5)
    assert result == ['text', 'duplicates', 'next', 'use', 'buttons']
    result = keywords_extraction(TEST_TEXT2, num_of_keys=5)
    assert result == ['test', 'testing', 'lorem', 'ipsum', 'test testing']
    result = keywords_extraction(TEST_TEXT3, num_of_keys=5)
    assert result == ['sit', 'amet', 'sit amet', 'ipsum', 'dolor']


def perform_tests():
    count_letters_test()
    count_words_test()
    ngrams_test()
    keywords_extraction_test()
    print("All test passed!")
