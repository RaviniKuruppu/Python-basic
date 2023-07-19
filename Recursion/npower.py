# Method 1
def npower(x,n):
    if n==0:
        return 1
    else:
        return x* npower(x, n-1)
print(npower(2, 5))


# Method 2 fast way
''''def npowerfast(x,n):
    if n==0:
        return 1
    elif n%2 ==0:
        hp=npowerfast(x,n/2)
        return hp*hp
    else:
        hp=npowerfast(x,n/2)
        return x*hp*hp
print(npowerfast(2, 10))'''