# 거스름 돈 N 분석
import time

start_time = time.time()  # 측정 시작

n, k = map(int, input("n, k 입력 : ").split())  # n, k 정수로 입력받기
coins = []  # 동전 담을 리스트
count = 0  # 횟수 셀 변수
for i in range(n):  # n번 반복하면서
    coin = int(input())  # 동전 입력받고, 정수로 변환
    coins.append(coin)  # 입력받은 값 리스트에 담기

coins.sort(reverse=True)  # 동전 역정렬 -> 큰 동전부터 정렬
print(coins)

for coin in coins:
    count += k // coin  # 해당 화폐로 거슬러 줄 수 있는 동전 개수 세기
    k %= coin  # 거슬러주고 남은 돈

print(count)

end_time = time.time()  # 측정 종료
print(f"시간복잡도 : {end_time - start_time}초")
