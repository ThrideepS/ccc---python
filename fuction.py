
# functions
def greet():
    print("Hello, World!")

print(greet()) # function returns None by default
Hello, World!
None
def greet(name):
    print("Hello, ", name)

greet("Thomas")
Hello,  Thomas
def print_num(a, b):
    print("a = ", a, "b = ", b)

# required arguments
print_num(115, 22)

# keyword arguments
print_num(b=22, a=115)

# print_num(b=22, 115) -> SyntaxError: positional argument follows keyword argument

def print_num(a, b, c=0): # c is a default argument
    print("a = ", a, "b = ", b, "c = ", c)

print_num(115, 22) # c is 0 by default
a =  115 b =  22
a =  115 b =  22
a =  115 b =  22 c =  0
# variable length arguments
def sum_of_nums(*nums):
    res = 0
    for num in nums:
        res += num
    return res

print(sum_of_nums(1, 2, 3, 4, 5))
15
def my_func():
    return ("Sami", "TypeScript", "Python", "JavaScript", "C++", 19)

name, *langs, age = my_func()
print(*langs)
TypeScript Python JavaScript C++
def outer():
    print("Hello from outer function")
    def inner():
        print("Hello from inner function")
    inner()

outer()
# inner() -> NameError: name 'inner' is not defined
def inner():
    print("Hello from global scoped inner function")

def outer():
    print("Hello from outer function")
    def inner():
        print("Hello from inner function")
    inner()

outer()
inner()
Hello from outer function
Hello from inner function
Hello from global scoped inner function
def outer():
    print("Hello from outer function")
    def inner():
        print("Hello from inner function")
    return inner

t = outer() # outer() returns inner function
t() # inner()
Hello from outer function
Hello from inner function
def recursive_func(n):
    if n > 0:
        recursive_func(n - 1) # head recursion
        print(n, end=" ")

recursive_func(5)
1 2 3 4 5 
def recursive_func(n):
    if n > 0:
        print(n, end=" ")
        recursive_func(n - 1) # tail recursion

recursive_func(5)
5 4 3 2 1 
def reverse_string(string):
    if string:
        print(string[-1], end="")
        reverse_string(string[:-1])

reverse_string("hi there")
ereht ih
p = 6
print("global p = ", p)
def outer():
    p = 7
    print("outer p = ", p)
    def inner():
        nonlocal p # nonlocal keyword is used to access outer scope variables
        p = 8
        print("inner p = ", p)
    inner()
    print("outer p = ", p)

outer()
print("global p = ", p)
global p =  6
outer p =  7
inner p =  8
outer p =  8
global p =  6
# anonymous functions
lst = [1, 2, 3]
res = list(map(lambda x: x * x, lst))
print(res)
[1, 4, 9]
# generate a list of factorials for each of the numbers in the list
import math
lst = [1, 2, 3]

res = list(map(math.factorial, lst))
print(res)
[1, 2, 6]
