f = float(input("소수점 5자리 이하 입력 :"))
print(round(f, 2))  # 소수점 2자리 출력, round 반올림 함수

a = float(input("소수를 5자리 이하 입력"))
print(format(a, ".2f"))  # format 함수 소수점 2자리 출력

a, b = map(float, input("소수 5자리 이하 2개 입력 : ").split())  # 실수 2개 입력받기
c = a / b
print("%0.3f" % c)

a, b, c = map(int, input().split())  # 정수 3개 입력받음
total = a + b + c  # 합
avg = total / 3  # 평균
print(total, format(avg, ".2f"))  # 합과 평균(소수점 2자리) 출력
