n,n1=input().split()
PG=abs(len(n)-len(n1))
for i in range(len(num)):
  if len(n1)==1 and n1[i] in n:
   break
  if n[i]!=n1[i]:
   PG+=1
print(PG)
