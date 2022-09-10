import datetime

now = datetime.datetime.now()

print(now)
print(f'Сегодня {now:%d} {now:%B} {now:%Y}')
print(f'{now:%H} {now:%M} {now:%S}')