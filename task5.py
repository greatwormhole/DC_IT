i = 0
s = []
while i < 5:
    s.append(int(input()))
    i += 1
s.sort(reverse=True)
i = 0
while i < 5:
    print(s[i])
    i += 1