import datetime

a, b, c = map(int, input().split())
d, e, f = map(int, input().split())

start_date = datetime.date(a, b, c)
target_date = datetime.date(d, e, f)
start_after_1000 = datetime.date(a + 1000, b, c)


d_day = target_date - start_date
print(f"D-{d_day.days}") if target_date < start_after_1000 else print('gg')