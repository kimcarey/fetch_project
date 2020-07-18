'''
Problem statement: Accept a string as input and return a response indicating whether a word is a pyramid word.  A word
is a ‘pyramid’ word if you can arrange the letters in increasing frequency, starting with 1 and continuing without gaps
and without duplicates.
Examples:
banana is a pyramid word because you have 1 'b', 2 'n's, and 3 'a's.
bandana is not a pyramid word because you have 1 'b' and 1 'd'.
'''

from collections import Counter


# # Using Counter (more efficient)
# def is_word_pyramid_counter(string):
#     word_count = Counter(string)
#     word_count_asc = sorted(word_count.items(), key=lambda i:i[-1])
#
#     return dict(word_count_asc)
#
#     # for i, (j, k) in enumerate(word_count_asc):
#     #     print(i, j, k)
#     #     if word_count_asc[k] != i + 1:
#     #         return False
#     #     else:
#     #         return True
#
# print(is_word_pyramid_counter('banana'))
# print(is_word_pyramid_counter('kimmy'))


def make_word_pyramid(word: str) -> Counter:
    assert len(word) <= 45, f"Your word must be less than 45 characters, but was {len(word)}"
    word_count = Counter(word.lower())
    return word_count


# print(make_word_pyramid('banana'))
# print(make_word_pyramid('skipit'))
# print(make_word_pyramid('skip it'))
# print(make_word_pyramid('skip-it'))



def is_valid_word_pyramid(pyramid:Counter) -> bool:
    i = 1
    for item in reversed(pyramid.most_common()):
        if item[1] != i:
            return False
        i += 1
    return True




# # Brute Force
# def is_word_pyramid(word: str):
#     seen = {}
#     for letter in word:
#         if letter in seen:
#             seen[letter] += 1
#         else:
#             seen[letter] = 1
#     return seen
#
# print(is_word_pyramid('banana'))

# Think of edge cases (what if you're given a really long string) - write up versions of the algorithm and use python built-in time it
# Write test




