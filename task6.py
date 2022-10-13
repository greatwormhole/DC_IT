l = list(set(input().lower().split(sep=", ")))
l.sort()
print(*l, sep=", ")