import time

start_time = time.time()  # 측정 시작

h = int(input())
count = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i) + str(j) + str(k):
                count += 1
print(count)

end_time = time.time()  # 측정 종료
print(f"시간복잡도 : {end_time - start_time}초")
