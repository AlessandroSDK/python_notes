# OrderedDict - Remember the insertion order of keys

>>> import collections
>>> d = collections.OrderedDict(one=1, two=2, three=3)

>>> d
OrderedDict([('one', 1), ('two', 2), ('three', 3)])

>>> d['four'] = 4
>>> d
OrderedDict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])

>>> d.keys()
odict_keys(['one', 'two', 'three', 'four'])

# collections.defaultdict - Return default values for missing keys

>>> from collections import defaultdict
>>> dd = defaultdict(list)

# Accessing a missing key creates it and initializes it
# using the default factory, i.e. list() in this example:
>>> dd['dogs'].append('Rufus')
>>> dd['dogs'].append('Kathrin')
>>> dd['dogs'].append('Mr Sniffles')

>>> dd['dogs']
['Rufus', 'Kathrin', 'Mr Sniffles']


# collections.ChainMap - Search multiple dictionaries as a single mapping

>>> from collections import ChainMap
>>> dict1 = {'one': 1, 'two': 2}
>>> dict2 = {'three': 3, 'four': 4}
>>> chain = ChainMap(dict1, dict2)

>>> chain
ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4})

# ChainMap searches each collection in the chain
# from left to right until it finds the key (or fails):
>>> chain['three']
3
>>> chain['one']
1
>>> chain['missing']
KeyError: 'missing'

# types.MappingProxyType - A wrapper for making read-only dictionaries

>>> from types import MappingProxyType
>>> read_only = MappingProxyType({'one': 1, 'two': 2})

>>> read_only['one']
1
>>> read_only['one'] = 23
TypeError: "'mappingproxy' object does not support item assignment"
