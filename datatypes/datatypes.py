#### Lists ####

my_list = [10, 20, 30, 40, 50]


#### Tuples ####
my_tup = (1,2,3,4,5,6,7,8,9,10)


#### Dictionaries ####
my_dict = {'name': 'Alex', 'age': '39', 'occupation': 'SRE'}

for key, val in my_dict.iteritems():
    print("My {} is {}".format(key, val))

squares = {x: x * x for x in range(10)}


#### Sets ####
my_set = {10,20,30,40,50,10,20,30,40,50}


quares = {x * x for x in range(10)}

>>> vowels = {'a', 'e', 'i', 'o', 'u'}
>>> 'e' in vowels
True

>>> letters = set('alice')
>>> letters.intersection(vowels)
{'a', 'e', 'i'}

>>> vowels.add('x')
>>> vowels
{'i', 'a', 'u', 'o', 'x', 'e'}

>>> len(vowels)
6

# An immutable version of set that cannot be changed after it was constructed. 

>>> vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
>>> vowels.add('p')
AttributeError: "'frozenset' object has no attribute 'add'"



#### Lists comprehention ####
my_list = [1,2,3,4,5,6,7,8,9,10]

squares = [num*num for num in my_list]
print(squares)
