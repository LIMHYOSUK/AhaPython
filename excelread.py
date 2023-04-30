import pandas as pd

# 엑셀 파일을 읽어와서 DataFrame으로 저장
df = pd.read_excel('파일명.xlsx')

# # '시트1' 시트의 내용을 읽어와서 DataFrame으로 저장
# df = pd.read_excel('파일명.xlsx', sheet_name='시트1')

# 2번째 열의 값을 출력
print(df.iloc[:, 1])

# 3번째 행의 값을 출력
print(df.iloc[2, :])
