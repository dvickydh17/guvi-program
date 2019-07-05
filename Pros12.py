from itertools import combinations
p,q=input().split()
q=int(q)
k=[]
cam=len(p)-q
fake=combinations(p,cam)
for i in list(fake):
  k.append("".join(i))
print(min(k))
