L = [x for x in input().split()]
L2=[]
for i in range(len(L)) :
    if i%2==0 :
        L2.append(L[i][::-1])
    else :
        L2.append(L[i])

print(*L2,end='')
