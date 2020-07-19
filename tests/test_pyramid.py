'''
Tests include:
- What Counter will return for:
    - Valid word pyramid
    - Invalid word pyramid
    - Hyphen included in string input
    - Space included in string input
    - Capital letters included in string input
    - Emoji / Unicode characters included in string input
    - Integers included in string input
    - Length of string input
'''

import pytest
import word_pyramid
from collections import Counter
from word_pyramid import create_app

class TestAlgorithm:
    def test_counter_banana(self):
        pyramid = word_pyramid.make_word_pyramid('banana')
        assert pyramid == Counter({'b': 1, 'n': 2, 'a': 3})

    def test_counter_bandana(self):
        pyramid = word_pyramid.make_word_pyramid('bandana')
        assert pyramid == Counter({'b': 1, 'd': 1, 'n': 2, 'a': 3})

    def test_counter_hyphen(self):
        pyramid = word_pyramid.make_word_pyramid('skip-it')
        assert pyramid == Counter({'s': 1, 'k': 1, 'p': 1, '-': 1, 't':1, 'i': 2})

    def test_counter_space(self):
        pyramid = word_pyramid.make_word_pyramid('hi there')
        assert pyramid == Counter({'i': 1, ' ': 1, 't': 1, 'r': 1, 'h': 2, 'e': 2})

    def test_counter_uppercase_letter(self):
        pyramid = word_pyramid.make_word_pyramid('SkipPeR')
        assert pyramid == Counter({'s': 1, 'k': 1, 'i': 1, 'e': 1, 'r': 1, 'p': 2})

    def test_counter_unicode(self):
        pyramid = word_pyramid.make_word_pyramid('☂')
        assert pyramid == Counter({'☂': 1})

    def test_input_integers(self):
        pyramid = word_pyramid.make_word_pyramid('1223334444')
        assert pyramid == Counter({'1': 1, '2': 2, '3': 3, '4': 4})

    def test_max_word_length(self):
        longest_word_english = 'pneumonoultramicroscopicsilicovolcanoconiosis'
        pyramid = word_pyramid.make_word_pyramid(longest_word_english)
        with pytest.raises(AssertionError) as e:
            pyramid = word_pyramid.make_word_pyramid(longest_word_english + 'a')
        assert e.value.args[0] == 'Your word must be less than 45 characters, but was 46'

    def test_is_valid(self):
        assert word_pyramid.is_valid_word_pyramid(Counter({'b': 1, 'n': 2, 'a': 3}))

    def test_not_valid(self):
        assert word_pyramid.is_valid_word_pyramid(Counter({'b': 1, 'd': 1, 'n': 2, 'a': 3})) == False


class TestAPI:
    # Use pytest-flask to specify an app fixture and send API requests with the app.
    # Create a fixture - app() - to create Flask server.
    @pytest.fixture
    def app(self):
        app = create_app()
        return app

    # Create a test client.
    @pytest.fixture
    def client(self, app):
        client = app.test_client()
        return client

    def test_valid(self, client):
        # Send a GET request with input string.
        response = client.get('/banana')
        # Check status code returned from server is 200 (OK).
        assert response.status_code == 200
        # Check that json returned is in correct format; is_valid_word_pyramid function should return True.
        assert response.json == {
            'word': 'banana',
            'isValidPyramid': True
        }

    def test_invalid(self, client):
        response = client.get('/bandana')
        assert response.status_code == 200
        # Check that json returned is in correct format; is_valid_word_pyramid function should return False.
        assert response.json == {
            'word': 'bandana',
            'isValidPyramid': False
        }

    def test_invalid_string_length(self, client):
        longest_word_english = 'pneumonoultramicroscopicsilicovolcanoconiosis'
        # Send GET request with string input that is greater than 45 chars.
        response = client.get(f"/{longest_word_english}_invalid")
        # Check that status code returned is 400 bad request.
        assert response.status_code == 400
        # Checks the error message (need to decode from byte string to ASCII).
        assert response.data.decode('ASCII') == 'Your word must be less than 45 characters, but was 53'
