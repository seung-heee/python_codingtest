# 그리디 - 거스름돈
"""음식점의 계산을 돕는 점원이 있다. 
거슬러 주어야 할 돈이 N원일 때 거슬러 주어야 할 동전의 최소 개수를 구하세요
참고 : 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.
참고 : 500원, 100원, 50원, 10원짜리 동전은 무한이 존재한다.
"""

import time
import psutil
import os

process = psutil.Process(os.getpid())  # 공간 복잡도를 위한 프로세스 id 얻기
start_time = time.time()  # 시간 측정 시작
n = 1260
count = 0

array = [500, 100, 50, 10]  # 거스름돈 줄 동전 담긴 리스트
for coin in array:
    count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전 개수 세기
    n %= coin  # 거슬러주고 남은 돈

print("동전의 거스름돈 최소 개수는 : ", count)

end_time = time.time()  # 측정 종료
print("time : ", format(end_time - start_time))
print("MB types : ", process.memory_info().rss / (1024.0 * 1024.0))
