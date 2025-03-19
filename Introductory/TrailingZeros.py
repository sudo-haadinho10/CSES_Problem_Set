
def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)

def TrailingZeros(n):
    #Legendres formula vp(n!)= Ek=1 to infiniti  [n/p^k]
    #it tells you how many times a specific prime number (like 2, 5, or any other prime) appears as a factor in (n!)

    ans=0
    p=5
    while(p<=n):
        ans+=n//p
        p*=5
    return ans

    

   
    

n=int(input())
#f=factorial(n)
z=TrailingZeros(n)
print(z)


