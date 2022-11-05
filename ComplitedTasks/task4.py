s = input().split(sep=' ')
ss = input().lower()
for c in s:
    if c.lower().find(ss) != -1:
        print(c)