# 일반 재귀함수로 피보나치 구현
import time

start_time = time.time()  # 측정 시작
# 실행 해 본 후 n을 30~50정도로 테스트
n = int(input("피보나치 n을 입력 : "))


def Fibonacci(num):
    if num == 0:
        return 0
    elif num == 2 or num == 1:
        return 1

    return Fibonacci(num - 2) + Fibonacci(num - 1)  # 점화식 표현 중요!


print(Fibonacci(n))
end_time = time.time()  # 측정 종료
print("시간복잡도 : ", end_time - start_time)
