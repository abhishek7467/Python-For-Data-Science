
def f3(num):
    res=1
    if num==1:
        return 1
    else:        
        res=(num*f3(num-1))
        return res

print(f3(5))

