def isPrime(n):
    if( n<2):
        return False
    i=2
    while i<=n//2:
        if (n%i==0):
            return False
        
        i=i+1
    return True

num=int(input("enter a digit"))

i=2
while i<=num:
    if (isPrime(i)):
        print(i)
    i=i+1