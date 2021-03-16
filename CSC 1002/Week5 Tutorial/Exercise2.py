inputstr=input("n numbers:")
inputsum=int(input("wanted sum:"))
alist=inputstr.split()
alist=alist(int(i) for i in alist)
alist.sort()
for value in alist:
    if value >= inputsum:
        indexnumber=alist.index(value)
        break
blist=alist[0:indexnumber+1:1]
for num1 in blist:
    