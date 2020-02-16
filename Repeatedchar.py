s = input()
L = []
for c in s:
    if c.isalpha() and s.count(c) <= 1:
        L.append(c.upper())
    else:
        L.append(c)
    res = ''.join(L)
    print(res)
        
