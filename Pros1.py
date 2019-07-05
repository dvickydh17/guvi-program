w= int(input())
c=[]
for i in range(0,w):
 inpu=input()
 c.append(input)
li=[]
for i in zip(*c):
 if(i.count(i[0])==len(i)):
  li.append(i[0])
 
 else:
  break
print(''.join(li))
