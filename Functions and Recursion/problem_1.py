def greatest(a,b,c):
    if(a > b and a > c):
        return a
    elif(b > c):
        return b
    else:
        return c

a = greatest(333,433,53)
print(a)