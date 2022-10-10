def is_empty(c):
    if c == '':
        return False
    return True


s = input().split(sep=' ')
ss = list(filter(is_empty, s))
l = len(ss)
for i in range(l):
    if i != 0:
        print('*', ss[i], sep='', end='')
    else:
        print(ss[0], end='')