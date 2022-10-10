l = input().lower().split(sep=", ")
s = list(set(l))
s.sort()
k = len(s)
for i in range(k):
    if i == k-1:
        print(s[i])
    else:
        print(s[i], end=", ")