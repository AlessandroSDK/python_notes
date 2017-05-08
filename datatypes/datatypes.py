# Lists

my_list = [10, 20, 30, 40, 50]

# Tuples
my_tup = (1,2,3,4,5,6,7,8,9,10)

# Dictionaries
my_dict = {'name': 'Alex', 'age': '39', 'occupation': 'SRE'}

for key, val in my_dict.iteritems():
    print("My {} is {}".format(key, val))

# Sets
my_set = {10,20,30,40,50,10,20,30,40,50}


# Lists comprehention
my_list = [1,2,3,4,5,6,7,8,9,10]

squares = [num*num for num in my_list]
print(squares)
