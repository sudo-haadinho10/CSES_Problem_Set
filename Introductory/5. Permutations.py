n=int(input())

if n==2 or n==3:
    print("NO SOLUTION")
elif n==1:
    print(1)
else:
    even=[i for i in range(1,n+1) if i%2==0]
    odd=[i for i in range(1,n+1) if i%2!=0]
    permutations=even+odd
    print(*permutations) #Unpack and print combined list seperated by spaces

