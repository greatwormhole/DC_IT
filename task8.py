s = input().split(sep='-')
month_codes = {'01': 1, '02': 4, '03': 4, '04': 0, '05': 2, '06': 5, '07': 0, '08': 3, '09': 6, '10': 1, '11': 4, '12': 6}
year_code = 6 + int(str(s[2][-2]) + str(s[2][-1])) + int(str(s[2][-2]) + str(s[2][-1])) // 4
a = (int(s[0]) + month_codes[s[1]] + year_code) % 7
if a == 0 or a == 1:
    print(f'{int(s[0]) - a - 5}-{s[1]}-{s[2]}')
else:
    print(f'{int(s[0]) - a + 2}-{s[1]}-{s[2]}')