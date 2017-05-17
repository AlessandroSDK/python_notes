# Here is a function that takes a value and returns the first key that maps to that value:

#def reverse_lookup(d, v):
#    for k in d:
#       if d[k] == v:
#           return k
#    raise ValueError

# Exercise 11.4. Modify reverse_lookup so that it builds and returns a list of all keys that map to v, or an empty list if there are none.

def reverse_lookup(d, v):
    key_list = []
    for k in d:
       if d[k] == v:
           key_list.append(k)
    return key_list

