# pip install pandas
# pip install openpyxl
import pandas as pd

###################################################################################
# excel 각 sheet를 DataFrame으로 저장
###################################################################################
"""################################################################################ 
1.pd.read_excel 함수는 기본적으로 첫 번째 행을 열 이름으로 간주합니다. 
  즉, 첫 번째 행에 데이터가 있는 경우 이를 열 이름으로 인식하게 되어 빈 데이터프레임이 출력됩니다.
  df1st = pd.read_excel('excelread-case1.xlsx', sheet_name='테이블목록', header=None)
################################################################################ """

df1st = pd.read_excel('excelread-case1.xlsx', sheet_name='테이블목록')
df2nd = pd.read_excel('excelread-case1.xlsx', sheet_name='컬럼정의서', header=None)

# 2번째 열의 값을 출력
print(df1st.iloc[:, 3])

# 3번째 행의 값을 출력
# print(df.iloc[2, :])

# print(df1st)
# print(df2nd)

###################################################################################
# DataFrame을 생성, 수정, 필터링, 그룹화, 정렬 및 집계하는 데 사용됩니다.
###################################################################################
"""
1. 생성 및 로딩 함수
pd.read_csv() : CSV 파일 읽기
pd.read_excel() : Excel 파일 읽기
pd.read_sql() : SQL 데이터베이스 읽기
pd.DataFrame() : DataFrame 생성

2.인덱싱 및 슬라이싱 함수
.loc[] : 라벨 기반 인덱싱 및 슬라이싱
.iloc[] : 정수 기반 인덱싱 및 슬라이싱
.at[] : 스칼라 값 액세스
.iat[] : 스칼라 값 액세스(정수 기반)

3.데이터 조작 및 변환 함수
.drop() : 열 또는 행 제거
.merge() : 두 DataFrame 병합
.groupby() : 열 값에 따라 그룹화
.pivot_table() : 데이터의 pivot 테이블 생성
.apply() : 사용자 정의 함수 적용
.fillna() : 결측값 대체
.replace() : 값 대체

4.데이터 분석 및 집계 함수
.describe() : 요약 통계량 계산
.count() : 결측값을 제외한 값의 개수 계산
.mean() : 평균값 계산
.median() : 중앙값 계산
.sum() : 합계 계산
.max() : 최대값 계산
.min() : 최소값 계산
.var() : 분산 계산
.std() : 표준편차 계산

5.시각화 함수
.plot() : 시각화
.hist() : 히스토그램 그리기
.boxplot() : 상자그림 그리기
.scatter() : 산점도 그리기
.heatmap() : 열지도 그리기
"""
