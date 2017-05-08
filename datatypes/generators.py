#Fibonacci generator
#def fib(n):
#    a,b = 0,1
#    for i in xrange(0, n):
#        yield a
#        a, b = b, a + b

#for item in fib(10):
#    print(item)

#Example generator
#def generator_function():
#    for i in range(10):
#        yield(i)

#for item in generator_function():
#    print(item)

#Example of an expensive Fibonacci sequence
#def fibon(n):
#    a = b = 1
#    result = []
#    for i in range(n):
#        result.append(a)
#        a, b = b, a + b
#    return result

#for i in fibon(1000000):
#   print i

def generator_function():
    for i in range(3):
        yield i

gen = generator_function()
print(next(gen))
# Output: 0
print(next(gen))
# Output: 1
print(next(gen))
# Output: 2
print(next(gen))
