# Trasversing a lists of strings and a lists of integers
cheeses = ['Cheddar', 'Brie', 'Parmisan', 'Blue']

for cheese in cheeses:
    print(cheese)

numbers = [10,20,30,40,50]

for number in range(len(numbers)):
   numbers[number] = numbers[number] * 2
   print numbers[number]


# Summing all numebrs in a list
# 1 solution
numbers = [10,20,30,40,50]

def add_all(t):
    total = 0
    for x in t:
        total += x
    return total

print add_all(numbers)

# 2 solution
print(sum(numbers))

# Trasversing a list building another one

names = ['alessandro','michele','paolo','emilio']

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

print(capitalize_all(names))

# Splitting and Joining

>>> s = 'pining for the fjords'
>>> t = s.split()
>>> print t
['pining', 'for', 'the', 'fjords']

>>> t = ['pining', 'for', 'the', 'fjords']
>>> delimiter = ' '
>>> delimiter.join(t)
'pining for the fjords'
