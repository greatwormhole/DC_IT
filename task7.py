s = input().split(sep=", ")
d = {}
for word in s:
    d[word] = d.get(word, 0) + 1
sorted_pairs = sorted(((key, value) for key, value in d.items()), key=lambda x: x[-1], reverse=True)
for pair in sorted_pairs[:3]:
    print(*pair, sep=": ")