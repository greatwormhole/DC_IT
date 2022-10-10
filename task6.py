l = input().lower().split(sep=", ")
s = list(set(l))
s.sort()
i = 0
k = len(s)
while i < k:
    if i == k-1:
        print(s[i])
    else:
        print(s[i], end=", ")
    i += 1