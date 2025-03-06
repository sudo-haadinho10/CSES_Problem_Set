n=int(input())

# if (type((n+1)/4)==float):
#     print("NO")
sum=int(n*(n+1)/2)
if sum%2==1:
    print("NO")
else:
    target=sum//2
    #print(target)
    print("YES")
    s1=[]
    s2=[]
    
    curr_sum=0
    for i in range(n,0,-1):
        if(curr_sum+i<=target):
            s1.append(i)
            curr_sum+=i
        else:
            s2.append(i)
    

         
    


            

    print(len(s1))
    print(" ".join(map(str,s1)))
    #print()
    print(len(s2))
    print(" ".join(map(str,s2)))



        



