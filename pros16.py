m = int(input())
l = list(map(int,input().split()))
count = 0
for i in range(m):
    for j in range(i,m):  
        for k in range(j,m):
            if l[i]<l[j]<l[k]:
                count+=1
print(count)
