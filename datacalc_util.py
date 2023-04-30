from datetime import date, datetime, time, timedelta


def get_vs_ta_ym_mnh_std(vd_ced):
    # 2월을 포함하는 다음 달 1일 계산
    if vd_ced.month == 12:
        next_month = datetime(vd_ced.year + 1, 1, 1)
    else:
        next_month = datetime(vd_ced.year, vd_ced.month + 1, 1)
    return next_month


vs_today = date.today().strftime("%Y%m%d")
# vs_ced = datetime.strptime(vs_today, "%Y%m%d").date()

vs_ced = vs_today                                     # 문자열타입 변환(YYYYMMDD)
vd_ced = datetime.strptime(vs_ced, '%Y%m%d').date()   # 날짜타입 변환(YYYY-MM-DD)

# vs_ta_y = vd_ced.strftime("%Y")                       # 기준년 YYYY
# vs_ta_m = vd_ced.strftime("%m")                       # 기준월 MM
# vs_ta_ym = vd_ced.strftime("%Y%m")                    # 기준년월 YYYYMM
# vs_ta_ym_std = vs_ced[0:6] + "01"                     # 기준년월 시작일자 YYYYMMDD
# relativedelta(months=1)).strftime("%Y%m")
vs_ta_ym_etd = (datetime.strptime(str(vs_ced)[0:6], "%Y%m"))

vs_ta_ym_mnh_std = get_vs_ta_ym_mnh_std(vd_ced).strftime("%Y%m%d")

print("vs_ta_ym_mnh_std : ", vs_ta_ym_mnh_std)
