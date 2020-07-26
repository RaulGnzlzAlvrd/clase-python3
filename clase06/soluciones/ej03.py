def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(s):
    if len(s) == 0:
        return True
    return first(s) == last(s) and is_palindrome(middle(s))


word = "redivider"
print(is_palindrome(word))
