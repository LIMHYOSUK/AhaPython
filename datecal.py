import datetime

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)

print(today, tomorrow)