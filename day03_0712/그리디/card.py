# nXm 배열 안에서 n행의 최솟값들을 뽑고 그 중 최댓값 추출하기

n, m = map(int, input().split())  # n행 m열 입력받기
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)  # 최솟값 추출
    result = max(result, min_value)
print(result)
