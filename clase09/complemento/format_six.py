def format_six(num):
    """
    0 -> "000000"
    23 -> "000023"
    1234567 -> "1234567"
    123456 -> "123456"
    """

    return str(num).zfill(6)
"""
    str_num = str(num)
    size = len(str_num)
    if size > 6:
        return str_num
    else:
        dif = 6 - size
        return "0" * dif + str_num
"""

assert format_six(0) == "000000"
assert format_six(23) == "000023"
assert format_six(1234567) == "1234567"
assert format_six(123456) == "123456"
