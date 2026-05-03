
import datetime

now = datetime.datetime.now()

print(now.year) #kuvab praeguse aasta
print(now.month) #kuvab praeguse kuu numbri (1-12)
print(now.day) #kuvab praeguse kuupäeva (1-31)
print(now.hour) #kuvab tunde (0-23)
print(now.minute) #kuvab minuti (0-60)

weekday = now.strftime("%a")
print(weekday)
