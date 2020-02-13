s = input()
l = []
for c in s :
    if c.isalpha() and s.count(c) > 1 :
        l.append(c.upper())
    else :
        l.append(c)
res = ''.join(l)
print(res,end='')
