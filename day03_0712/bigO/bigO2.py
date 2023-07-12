import time
import random

start_time = time.time()  # 측정 시작
array = []  # 리스트 생성

for v in range(2000):  # 시간 복잡도가 O(N^2)인 알고리즘
    array.append(random.randint(0, 10))  # 랜덤 값 추가

for i in array:
    for j in array:
        temp = i * j
        # print(temp)

print(temp)  # 측정 최종 값 출력
end_time = time.time()  # 측정 종료
print("time : ", end_time - start_time)
