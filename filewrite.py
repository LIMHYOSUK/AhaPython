#위 코드에서 open 함수는 c:/aa.txt 경로에 새 파일을 생성하고, 쓰기 모드("w")로 파일을 엽니다. with 문을 사용하면 블록 내에서 #파일을 작업한 후 자동으로 닫을 수 있습니다. 마지막으로 write 메소드를 사용하여 "abcdefg" 문자열을 파일에 씁니다. 이렇게 하면 #c:/aa.txt 파일이 생성되고 내용으로 "abcdefg" 문자열이 포함됩니다.

text = input("문자열을 입력하세요: ")

#1.file write
#with open("c:/AhaPython/Filewrite/aa.txt", "w") as file:

#2.file 끝에 append로 write
#with open("c:/AhaPython/Filewrite/aa.txt", "a") as file:

#3. file 다음줄에 append로 write
with open("c:/AhaPython/Filewrite/aa.txt", "a") as file:
    #file.write(text)
    file.write("\n" + text)