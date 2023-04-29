import csv

# csv 파일 경로
csv_file_path = "c:/AhaPython/Fileread/fileread.csv"

# csv 파일 열기
with open(csv_file_path, "r", newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

#    # 각 줄마다 출력
#    for row in csv_reader:
#        print(row)
        
    # 각 줄마다 출력
    for i, row in enumerate(csv_reader):
        # if i == 2:  # 세 번째 row
        #     print(row[2])  # 세 번째 인덱스 출력
        #     break  # 출력 후 종료
        if i == 0:
            col1, col2, col3, col4 = row        
            
            print("col1 : ", col1)
            print("col2 : ", col2)
            print("col3 : ", col3)
            print("col4 : ", col4)
            