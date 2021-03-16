# input number
nums = []


def promptNumber():
    idx = 1
    while True:
        n = input('enter '+str(idx)+' number:')
        if n == "x":
            break
        try:
            n = eval(n)
            if type(n) in (int, float):
                nums.append(n)
                idx += 1
        except:
            continue


# compare&print

def findmax(alist, c):
    ans = alist[0]
    for val in alist[1:]:
        ans = c(val, ans)
    print(ans)


promptNumber()
findmax(nums, max)
findmax(nums, min)
