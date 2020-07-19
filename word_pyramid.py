"""
Problem statement: Accept a string as input and return a response indicating whether a word is a pyramid word.  A word
is a ‘pyramid’ word if you can arrange the letters in increasing frequency, starting with 1 and continuing without gaps
and without duplicates.
Examples:
banana is a pyramid word because you have 1 'b', 2 'n's, and 3 'a's.
bandana is not a pyramid word because you have 1 'b' and 1 'd'.

ASSUMPTIONS:
- Assumes English language, but will accept any string as a "word"
- Capital letters should be turned into lower case
- Emoji / Unicode characters are treated as part of the word
- Integers are treated as part of the word
- Spaces and hyphens are treated as part of the word
- Assumes word length will not exceed 45 characters (if it does, code will raise an exception)

"""

from collections import Counter
from flask import Flask, jsonify, abort, Response


def create_app() -> Flask:
    """
    Create the Flask app and set up the API endpoint.

    :return: The Flask app.
    """
    app = Flask(__name__)

    # Route can take any string input in URL (dynamic route).
    @app.route('/<word>')
    def word_pyramid(word: str):
        """
        :param word: Any string less than 45 chars will be evaluated for word pyramid validity.
        :return: JSON containing the word and whether or not it's valid.
        """
        # Wrap make_word_pyramid() in try statement since there are conditions (must be <= 45 chars).
        try:
            # Call make_word_pyramid() function and store in variable for future use.
            pyramid = make_word_pyramid(word)

        # If string input exceeds 45 chars, throw an exception and abort request.
        except AssertionError as e:
            # Pass along message from exception with the 400 code so client knows what went wrong.
            abort(Response(str(e), 400))
            return
        # Call is_valid_word_pyramid() function and store in variable for future use.
        is_valid = is_valid_word_pyramid(pyramid)
        # Return response in JSON format.
        return jsonify({
            'word': word,
            'isValidPyramid': is_valid,
        })
    # Return an instance of a Flask app instead of creating one globally.
    return app


def make_word_pyramid(word: str) -> Counter:
    """
    Prepare a word pyramid by counting each character in a string.

    :param word: Any string less than 45 chars will be evaluated word pyramid validity.
    :raises AssertionError: When string is greater than 45 chars.
    :return: The pyramid (may not be valid).
    """
    assert len(word) <= 45, f"Your word must be less than 45 characters, but was {len(word)}"

    # Use built-in collections.Counter class to keep track of counts for each character in the string.
    # Counter should be more efficient than using dict manually.
    # Convert all letters from input string to lowercase (see ASSUMPTIONS).
    word_count = Counter(word.lower())
    return word_count


def is_valid_word_pyramid(pyramid:Counter) -> bool:
    """
    Checks if the given word pyramid is valid.
    E.g. banana is a pyramid word because you have 1 'b', 2 'n's, and 3 'a's. bandana is not a pyramid word because
    you have 1 'b' and 1 'd'.

    :param pyramid: Counter object (dictionary).
    :return: Boolean (True if word meets the conditions of a word pyramid; False if not).
    """
    # Set i to 1 since each letter in the counter will have at least 1 count.
    i = 1
    # Loop through each item in counter.
    # Counter is always displayed in descending order; use reversed() to sort values in ascending order.
    for item in reversed(pyramid.most_common()):
        # To be a valid word pyramid, count values for unique letters should be incrementing by 1. Therefore, the
        # value (which represents the letter count) should match i.
        # If the value doesn't match i, then word is not a valid word pyramid (return False).
        if item[1] != i:
            return False
        # Increment i by 1 for each go through the loop.
        i += 1
    # If loop ends and all conditions are met, then word is a valid word pyramid (return True).
    return True


if __name__ == '__main__':
    app = create_app()
    app.run('0.0.0.0', port=5000)
