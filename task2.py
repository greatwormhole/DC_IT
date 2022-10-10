s = input()
res = 0
while s:
    if int(s) % 2 == 0:
        res += int(s)
    s = input()
print(res)