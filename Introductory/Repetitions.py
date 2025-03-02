string1=input()
rep=1
p_rep=1

for i in range(0,len(string1)-1):
    if(string1[i]==string1[i+1]):
        p_rep+=1    
    if(p_rep>rep):
        rep=p_rep
    if(string1[i]!=string1[i+1]):
        p_rep=1


        


print(rep)

