No,No1=map(int,input().split())
for i in range(No+1,No1):
  sum=0
  No2=i
  while(No2>0):
    x=No2%10
    No2=No2//10
    y=x**3
    sum=sum+y
  if(i==sum):
    print(sum,end=' ')
