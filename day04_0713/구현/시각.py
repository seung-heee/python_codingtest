import time

start_time = time.time()  # 측정 시작

h = int(input())
count = 0

for i in range(h + 1):  # 시
    for j in range(60):  # 분
        for k in range(60):  # 초
            if "3" in str(i) + str(j) + str(k):  # 3 있는지 확인
                count += 1  # 있으면 +1
print(count)

end_time = time.time()  # 측정 종료
print(f"시간복잡도 : {end_time - start_time}초")
