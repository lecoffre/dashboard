import calendar, datetime

now = datetime.datetime.now()
alldays = calendar.monthrange(now.year, now.month)[1]
list_d = []
for i in range(alldays):
    list_d.append(str(i+1)+"/"+str(now.month)+"/"+str(now.year))

print(list_d)