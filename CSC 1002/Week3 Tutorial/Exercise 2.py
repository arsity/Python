# Week 3 Tutorial, Exercise 2.
# • Ask the user for a number. Print out a message to tell the
# user whether the number is even or odd. (Hint: how does
# an even / odd number react differently when divided by 2?)
# • If the number is a multiple of 4, print a different message.
# • Ask the user for two numbers: one is the numerator (call it
# num) and the other is the denominator (call it check). If
# check divides evenly into num, tell the user; if not, print a
# different message.

check = int(input("Please input the denominator:\n"))
num = int(input(
    "Please input the numerator to know that whether it can be divided by "+str(check)+":\n"))
mod = num % check
if check > num:
    print("The numerator must be bigger than denominator. Please check the number you typing in and restart the program.")
else:
    if mod == 0:
        print("%s can be divided evenly by %s." % (num, check))
    else:
        print("%s cannot be divided evenly by %s." % (num, check))
