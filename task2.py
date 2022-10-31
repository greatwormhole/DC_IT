from sys import stdin
print(sum([int(i) for i in filter(lambda x: x != '', map(str.strip, stdin)) if int(i) % 2 == 0]))