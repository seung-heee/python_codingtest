x = int(input())

d = [0] * 30001  # DP 테이블 초기화, 크기 지정

# 다이나믹 프로그래밍 진행,, 보텀업!
for i in range(2, x + 1):
    d[i] = d[i - 1] + 1  # 현재의 수에서 -1,, why????
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
