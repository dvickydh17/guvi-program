import math
s = str(input())
l = []
for i in s.split(" "):
    l1 = int(len(i))
    l.append(l1)
    c = len(l)
    s = sum(l)
print(math.ceil(s/c))
