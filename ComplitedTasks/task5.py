s = []
for i in range(5):
    s.append(int(input()))
s.sort(reverse=True)
print(*s, sep='\n')