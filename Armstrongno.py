num=int(input())
p=0
h=num
while h>0:
  digit = h%10
  p += digit **3
  h //=10
if num==p:
  print("yes")
else:
  print("no")
