import time
import sys

start_time = time.time()  # 측정 시작
# DP 메모제이션 기법으로 피보나치 구현

# n = int(sys.stdin.readline()) 더 빠른 입력 방식
N = int(input())  # 실행 해 본 후 n을 30~50정도로 테스트

arr = [0 for _ in range(N + 1)]  # 임시 공간 리스트 생성, 초기화
arr[1] = 1  # 0, 1로 시작

for i in range(2, N + 1):  # 피보나치 2부터 유효
    arr[i] = arr[i - 1] + arr[i - 2]  # 바로 값을 가져옴

print(arr[-1])

# 리스트에 때려넣고 최종 결과만 가져옴 : 메모이제이션
# 메모리에 값을 저장하여 중복 계산을 제거함, 계산을 재사용!
end_time = time.time()  # 측정 종료
print("시간복잡도 : ", end_time - start_time)
