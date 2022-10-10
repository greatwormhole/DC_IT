s = []
for i in range(5):
    s.append(int(input()))
s.sort(reverse=True)
for i in range(5):
    print(s[i])