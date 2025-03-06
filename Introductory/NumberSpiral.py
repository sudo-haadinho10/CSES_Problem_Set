n=int(input())
for i in range(n):
    y,x=map(int,input().split(' '))
    z=max(y,x)
    square=z**2

    

    if z%2!=0:
        if x==z:
            out=square-(y-1)
        else:
            #out=(square -(z-1))-(y-1)
            out=(square - (z-1))-(y-x)

        print(out)

    else:
        if y==z:
            out=square-(x-1)
        else:
            out=(square-(z-1))-(x-y)

        print(out)



