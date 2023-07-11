a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(a[3])  # 4

n = 10
b = [0] * n  # 크기가 n이고 모든 값이 0인 1차원 리스트가 만들어져요~
print(b)

print(a[-1])  # 맨 뒤
print(a[-3])

a[3] = 7  # 네번째 원소 값 변경
print(a)  # 변경된 값 확인
print(a[1:4])

array = [i for i in range(10)]  # 0~9까지의 수를 넣어 초기화
print(array)  # 0~9까지의 수를 가진 배열이 만들어짐

# 0~9까지의 수 중 홀수만 배열 array에 넣어 초기화
array = [i for i in range(10) if i % 2 == 1]
print(array)  # 1,3,5,7,9

array = []
for i in range(10):  # 0~9까지의 수 반복
    if i % 2 == 1:  # 홀수면
        array.append(i)  # 배열에 추가

print(array)
