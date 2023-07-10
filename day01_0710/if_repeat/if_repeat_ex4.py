# 문제1 : 정수(1 ~ 100) 1개를 입력 받아 1부터 그 수까지 짝수의 합을 출력하시오.
count = 0  # 짝수의 합을 담을 변수 count 선언
num = int(input("정수 1개 입력 : "))  # 1~num까지의 합을 구하기 위한 num값

for i in range(1, num + 1):  # 1~num까지 반복
    if i % 2 == 0:  # 짝수면
        count += i  # count에 해당 숫자(짝수) 담기
print(f"1부터 {num}까지의 합 : {count}")  # 출력

# 문제2 : 영문 소문자 q가 입력될 까지 입력 문자를 무한 출력하시오.
while True:  # 무한반복
    num = input("영문자를 입력하세요! : ")  # 문자열 입력받고
    if num == "q":  # q면
        break  # 종료
