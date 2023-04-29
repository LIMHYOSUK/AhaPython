import datetime
#########################################################################################
# timedelta --시간 차이를 나타내는 파이썬의 내장 클래스
#           > datetime 모듈에서 제공
#           > timedelta 객체를 생성하려면, datetime.timedelta() 생성자 함수를 사용
#########################################################################################
# days        : 일(day) 단위로 지정하는 정수형 매개변수입니다.
# seconds     : 초(second) 단위로 지정하는 정수형 매개변수입니다.
# microseconds: 마이크로초(microsecond) 단위로 지정하는 정수형 매개변수입니다.
# milliseconds: 밀리초(milliseconds) 단위로 지정하는 정수형 매개변수입니다.
# minutes     : 분(minute) 단위로 지정하는 정수형 매개변수입니다.
# hours       : 시(hour) 단위로 지정하는 정수형 매개변수입니다.
# weeks       : 주(week) 단위로 지정하는 정수형 매개변수입니다.
#########################################################################################

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)

print(today, tomorrow)


from datetime import date, timedelta

today = date.today()
yyyymmdd = today.strftime("%Y%m%d")

# 현재 날짜의 연도와 월 구하기
year = today.year
month = today.month

# 해당 월의 다음달 구하기
if month == 12:
    next_month = date(year + 1, 1, 1)
else:
    next_month = date(year, month + 1, 1)

# 해당 월의 말일자 구하기
last_day = (next_month - timedelta(days=1)).day

print("Today's date in yyyymmdd format:", yyyymmdd)
print("Last day of the month:", last_day)
