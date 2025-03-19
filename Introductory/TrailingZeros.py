
def TrailingZeros(n):
    #Legendres formula vp(n!)= ∑ (k=1 to infiniti)  [n/p^k] 
    #[x] -> depict floor function gives the largest integer >=x(real number)
    #It lyk how many times a specific prime number (p) like 2, 5, or any other prime appears as a factor in (n!)

    ans=0
    p=5
    while(p<=n):
        ans+=n//p
        p*=5
    return ans

    

   
    

n=int(input())
z=TrailingZeros(n)
print(z)


