"""N이 1이 될 때까지 두 과정 중 하나를 반복적으로 선택 수행하는 방법은? 최소값을 출력하시오.
참고 : 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.
참고 : N에서 1을 뺀 후, N을 K로 나눈다.
"""
import time

start_time = time.time()  # 측정 시작
# n, k = map(int, input("n, k를 입력하세요 : ").split())
n = 25
k = 3
count = 0

while n != 1:  # n이 1이면 종료
    if n % k == 0:  # 나눠지면
        n //= k  # 나눈 후의 몫을 넣기
        count += 1  # 연산 횟수 증가
        print("N을 k로 나누기 : ", n)
    else:  # 나눠지지 않으면
        n -= 1  # 1을 뺀다.
        count += 1  # 연산 횟수 증가
        print("N에서 1빼기 : ", n)

print("총 연산 횟수 :", count)

end_time = time.time()  # 측정 종료
print(f"시간복잡도 : {end_time - start_time}초")
