"""
12. Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed.
"""


def is_palindrome(word):
    letters = list(word)
    letters.reverse()
    rev = ''.join(letters)
    return word == rev


if __name__ == '__main__':
    word = "rar"
    if is_palindrome(word):
        print('Is palindrome')
    else:
        print('Not a palindrome')
