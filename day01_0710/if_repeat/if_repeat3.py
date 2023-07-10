# 중첩 if문
n = int(input("정수 1개 입력 : "))
if n < 0:  # 홀수
    if n % 2 == 0:  # 짝수
        print("음수, 짝수 : ", n)
    else:  # 홀수
        print("음수, 홀수 : ", n)
else:  # 짝수
    if n % 2 == 0:
        print("양수, 짝수 : ", n)
    else:
        print("양수, 홀수 : ", n)


# 점수 입력받기
score = int(input("점수 입력 : "))
