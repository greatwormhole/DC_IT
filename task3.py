def is_empty(c):
    if c == '':
        return False
    return True


s = input().split(sep=' ')
ss = list(filter(is_empty, s))
i = 0
l = len(ss)
while i < l:
    if i != 0:
        print('*', ss[i], sep='', end='')
    else:
        print(ss[0], end='')
    i += 1