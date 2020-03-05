def f(L):
    for x in range(1,len(L)):
        thing=L[x]
        print(thing)
        y=x-1
        print(y)

        while (y>=0) and (thing < L[y]):
            L[y+1]=L[y]
            y -= 1
            print(y)

        L[y+1]=thing

mylist=[12,11,13,5,6]
f(mylist)
print(mylist)
        
        
