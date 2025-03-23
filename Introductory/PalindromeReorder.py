n=input()

single=[]
pair=[]

for char in n:
    if char in single:
        single.remove(char)
        pair.append(char)
    else:
        single.append(char)

palindrome=''.join(pair)+''.join(single)+''.join(pair[::-1])

if(palindrome==palindrome[::-1]):
    print(palindrome)
else:
    print("NO SOLUTION")
