#Objective: Use recursion to implement a function that calculates the factorial of a number
#Recursion is a really cool and powerful application of computer science.
#More specifically, recursion allows you to define a function that is able to call itself.
#The example below is a good illustration of how simple it can be to calculate something that would otherwise be pretty complex.
#Imagine if our n were 1000... could be quite a pain... but recursion makes it quick and easy.

#Task 
#Write a factorial function that takes a positive integer, as a parameter and prints the result of (factorial).


# Below, function takes an input 
n = int(input())

# factorial function defined
def factorial(n):
    # next line is the base case
    if n <= 1:
        return 1
    # next line is the recursive case
    else: 
        return n * factorial(n-1)

# Next line allows you to print the output of your function, given the input n
print(factorial(n))




