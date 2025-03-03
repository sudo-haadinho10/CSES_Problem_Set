n=int(input())
arr1=[int(x) for x in input().split(' ')]
best=arr1[0]
sum=0

for k in range(0,len(arr1)):
    sum=max(arr1[k],sum+arr1[k])
    best=max(sum,best)
    
    
print(best)
