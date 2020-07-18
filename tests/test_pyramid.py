'''
EDGE CASES
Internationalization - am I only getting English characters?
How to deal with capitalization
How to deal with spaces and hyphens
Look up longest word in english language and set a limit to word length that will be accepted

OTHER:
Set up CircleCI (continuous integration) to automatically run tests when a commit is made

'''

import pytest
import word_pyramid
from collections import Counter

def test_counter_banana():
    pyramid = word_pyramid.make_word_pyramid('banana')
    assert pyramid == Counter({'b': 1, 'n': 2, 'a': 3})

def test_counter_bandana():
    pyramid = word_pyramid.make_word_pyramid('bandana')
    assert pyramid == Counter({'b': 1, 'd': 1, 'n': 2, 'a': 3})

def test_counter_hyphen():
    pyramid = word_pyramid.make_word_pyramid('skip-it')
    assert pyramid == Counter({'s': 1, 'k': 1, 'p': 1, '-': 1, 't':1, 'i': 2})

def test_counter_space():
    pyramid = word_pyramid.make_word_pyramid('hi there')
    assert pyramid == Counter({'i': 1, ' ': 1, 't': 1, 'r': 1, 'h': 2, 'e': 2})

def test_counter_uppercase_letter():
    pyramid = word_pyramid.make_word_pyramid('SkipPeR')
    assert pyramid == Counter({'s': 1, 'k': 1, 'i': 1, 'e': 1, 'r': 1, 'p': 2})

def test_max_word_length():
    longest_word_english = 'pneumonoultramicroscopicsilicovolcanoconiosis'
    pyramid = word_pyramid.make_word_pyramid(longest_word_english)
    with pytest.raises(AssertionError):
        pyramid = word_pyramid.make_word_pyramid(longest_word_english + 'a')

def test_is_valid():
    assert word_pyramid.is_valid_word_pyramid(Counter({'b': 1, 'n': 2, 'a': 3}))

def test_not_valid():
    assert word_pyramid.is_valid_word_pyramid(Counter({'b': 1, 'd': 1, 'n': 2, 'a': 3})) == False