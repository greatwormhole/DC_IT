s = input().split(sep=", ")
d = {}
for word in s:
    if word not in list(d.keys()):
        d.update({word: 1})
    else:
        d[word] += 1
sorted_keys = sorted(d, key=d.get, reverse=True)
sorted_dict = {}
for i in sorted_keys:
    sorted_dict[i] = d[i]
i = 0
temp = list(sorted_dict.keys())
while i < 3 and i < len(temp):
    print(f'{temp[i]}: {sorted_dict.get(temp[i])}')
    i += 1