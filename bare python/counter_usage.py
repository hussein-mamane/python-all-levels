from collections import Counter

# from mapping, from keywords, from iterable
c_mapping = Counter({'red': 4, 'blue': 2})
c_keyword = Counter(cats=4, dogs=8)
c_iterable_string = Counter("Hello")
c_iterable_array = Counter(['eggs', 'ham'])

# counter methods
print(c_iterable_string.most_common())
print(c_iterable_string.most_common(3))
print(c_iterable_string.elements())  # itertools.chain
print(sorted(c_iterable_string.elements()))  # list
print(sorted(c_iterable_array.elements()))  # list
print(c_iterable_string["p"])
del (c_iterable_string["o"])
print(sorted(c_iterable_string.elements()))

# substract
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)

# total
print(f"{c.total()=}")
# fromkeys is not implemented for Counter

# update(non-nested iterable)
c.update(['a', 'a', 'y', "I've a bike"])
print(c)

"""
c.total()                       # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
+c                              # remove zero and negative counts
"""
"""
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
c + d                       # add two counters together:  c[x] + d[x]
Counter({'a': 4, 'b': 3})
c - d                       # subtract (keeping only positive counts)
Counter({'a': 2})
c & d                       # intersection:  min(c[x], d[x])
Counter({'a': 1, 'b': 1})
c | d                       # union:  max(c[x], d[x])
Counter({'a': 3, 'b': 2})
c == d                      # equality:  c[x] == d[x]
False
c <= d                      # inclusion:  c[x] <= d[x]
False
"""

c.clear()
print(c)
