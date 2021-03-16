# Week 3 Tutorial, Exercise 1.
# • Create a program that asks users to enter their names and
# ages. Print out a message that tells them the year when
# they turn 100 years old.
# • Ask the user for a number of times that they wish to repeat
# that message. Then print out that many copies of the
# previous message.
# • Print out every message on a new line. (Hint: the string "\n”
# is the same as pressing the ENTER button)

TIME_NOW = 2021
HOW_OLD = 100
HOW_OLD = str(HOW_OLD)
name = input("Please input your name:\n")
age = int(input("Please input your age:\n"))
year = TIME_NOW+100-age
year = str(year)
message = name+" will be "+HOW_OLD+" years old in "+year+".\n"
times = int(input("How many times do you want to print:\n"))
print(message*times)
