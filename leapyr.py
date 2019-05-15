yea=int(input())
if((yea%400==0) or (yea%4==0) and (yea%100!=0)):
    print("yes")
else:
    print("no")
