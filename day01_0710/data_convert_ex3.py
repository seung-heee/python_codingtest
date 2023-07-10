# 정수 3개 입력 받아 합과 평균 출력
a, b, c = map(int, input("정수 3개 입력 : ").split())
sub = a + b + c
avg = sub / 3
print("sub : ", sub)  # 합
print("avg : ", format(avg, ".2f"))  # 평균
