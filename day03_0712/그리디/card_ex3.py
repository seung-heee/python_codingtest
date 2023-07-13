import random

# N, M = map(int, input("N, M을 입력해라: ").split())
array = [[3, 1, 2], [4, 1, 4], [2, 2, 2]]
# for n in range(N):
#   array.append(random.randint(0, 10))  # 랜덤 값 추가

array1 = [3, 1, 2]
array2 = [4, 1, 4]
array3 = [2, 2, 2]

min1 = min(array1)
min2 = min(array2)
min3 = min(array3)

mins = [min1, min2, min3]  # 최솟값 모아두기~
maxAll = max(mins)  # 최솟값 중 최댓값 찾기

print(maxAll)
