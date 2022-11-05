from datetime import datetime as dt
s = dt.strptime(input(), "%d-%m-%Y")
print("{}-{:02}-{}".format(s.day - s.weekday(), s.month, s.year))