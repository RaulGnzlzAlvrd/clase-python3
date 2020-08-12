def in_bisect(t, query):
    """
    Busca el elemento query en la lista ordenada t

    t: listof a
    query: a
    return: boolean
    """
    size = len(t)
    index = size // 2
    if size == 0:
        return False
    candidate = t[index]
    if candidate == query:
        return True
    if candidate < query:
        return in_bisect(t[index+1:], query)
    else:
        return in_bisect(t[:index], query)
