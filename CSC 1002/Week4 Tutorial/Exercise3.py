list1 = list(input("INPUT1:"))
list2 = list(input("INPUT2:"))
list1.sort()
list2.sort()
if list1 == list2:
    print("ANAGRAM")
else:
    print("!ANAGRAM")
