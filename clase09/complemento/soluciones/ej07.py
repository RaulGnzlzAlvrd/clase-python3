def format_six(num):
    return str(num).zfill(6)

def is_palindrome(word):
    return word == word[::-1]

def pass_check(num, start, end):
    return is_palindrome(format_six(num)[start:end])

def odometer_palindrome(num):
    if not pass_check(num, -4, 6):
        return False
    if not pass_check(num + 1, -5, 6):
        return False
    if not pass_check(num + 2, 1, 5):
        return False
    if not pass_check(num + 3, 0, 6):
        return False
    return True

for i in range(0, 1000000):
    if odometer_palindrome(i):
        print(format_six(i))
