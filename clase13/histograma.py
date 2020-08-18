def histograma(s):
  d = dict()
  for c in s:
    d[c] = d.get(c, 0) + 1
  return d
