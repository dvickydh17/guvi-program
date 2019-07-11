k,q=map(str,input().split())
r=0
if len(k)>len(q):
    k,q=q,k
s=0
while s<len(k):
      r+=(ord(q[s])-ord(k[s]))
      s+=1
for s in range(s,len(q)):
      r+=ord(q[s])-ord('a')+1
print(r)
