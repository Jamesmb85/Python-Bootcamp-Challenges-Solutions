# Problem 1
# Create a generator that generates the squares of numbers up to some number N.
def gensquares(N):
    for value in range(N):
        yield value**2

# Problem 2
# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
import random
def rand_num(low,high,n):
    for value in range(n):
        yield random.randint(low, high)


# Problem 3
# Use the iter() function to convert the string below into an iterator:
s = 'hello'
iteration_string = iter(s)
print(next(iteration_string))
print(next(iteration_string))
print(next(iteration_string))
print(next(iteration_string))
print(next(iteration_string))
#print(next(iteration_string)) running this line will cause a StopIteration exception


# Problem 4
# Explain a use case for a generator using a yield statement where you would not want
# to use a normal function with a return statement.

""""
Anytime you don't need to occupy memory such as using an Array.
For example, if we need to iterate or any iterable, but don't need to store the information for later use, we use
a generator. 
"""


# Extra Credit!
# Can you explain what gencomp is in the code below? (Note: We never covered this in lecture!
# You will have to do some Googling/Stack Overflowing!)

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)

# Generator Expressions are somewhat similar to list comprehensions, but the former doesn’t construct list object.
# Instead of creating a list and keeping the whole sequence in the memory, the generator generates the next element in demand.
# When a normal function with a return statement is called, it terminates whenever it gets a return statement.
# But a function with a yield statement saves the state of the function and can be picked up from the same state,
# next time the function is called.
# The Generator Expression allows us to create a generator without the yield keyword.









