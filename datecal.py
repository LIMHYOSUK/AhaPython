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