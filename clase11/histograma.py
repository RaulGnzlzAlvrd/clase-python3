def histograma(s):
  d = dict()
  for c in s:
    d[c] = d.get(c, 0) + 1
    """
    if c not in d:
      d[c] = 1
    else:
      d[c] += 1
    """
  return d
