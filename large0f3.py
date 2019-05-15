va1,va2,va3=input().split()
va1=int(va1)
va2=int(va2)
va3=int(va3)
if(va1>va2 and va1>va3):
    print(va1)
elif(va2>va3):
    print(va2)
else:
    print(va3)
