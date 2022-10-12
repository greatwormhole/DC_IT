l = list(set(input().lower().split(sep=", ")))
l.sort()
k = len(l)
for i in range(k):
    if i == k-1:
        print(l[i])
    else:
        print(l[i], end=", ")