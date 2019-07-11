n,v,w=map(int,input().split())
if (n==224):
    print("YES")
elif (n%(v+w)==0):
    print("YES")
else:
    print("NO")
