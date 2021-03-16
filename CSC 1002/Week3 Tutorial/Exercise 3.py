# Week 3 Tutorial, Exercise 3.
# • Ask the user for a string . Print out whether it is a
# palindrome or not. (A palindrome is a string that reads the
# same forwards and backwards.)
# • Note: Python has its built-in reserve function, but DO NOT
# USE IT FOR NOW!

word = input("Please input the word to check whether it is a palindrome:\n")
rvs = word[::-1]
if rvs == word:
    print(word+" is a palindrome.")
else:
    print(word+" is not a palindrome.")
