l=list(map(int,input("enter numbers").split()))
print(l)

def sortnum(l):
    n=len(l)
    i=0
    while i<n:
        j=i+1
        while j<n:
            if (l[i]>l[j]):
                temp=l[j]
                l[j]=l[i]
                l[i]=temp
            j=j+1   
        i=i+1
    return l

print(sortnum(l))
print()