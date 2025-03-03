from typing import List
import sys

input = sys.stdin.readline


size,targsum=map(int,input().split(' '))
arr1=list(map(int,input().split()))

b=arr1[:]
b.sort()
p,q=None,None
l,r=0,size-1
while l<r:
    while l<r and  b[l]+b[r]>targsum:
        r-=1
    
    if l<r and b[l]+b[r]==targsum:
        p,q=b[l],b[r]
        break
    l+=1
    

if p is None:
    print("IMPOSSIBLE")
else:
    l=arr1.index(p)
    r = arr1.index(q) if p != q else arr1.index(p, l + 1)


    print(l+1,r+1)
