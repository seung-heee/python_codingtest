a, b = map(int, input("입력한 두 정수의 큰 값 판단 : ").split())
if a > b:
    print(a)
else:
    print(b)

a, b = map(int, input("두 정수 입력2 : ").split())
c = a if a >= b else b
print(c)

a, b, c = map(int, input("정수 3개 입력 : ").split())
print("최솟값 : ", min(a, b, c))  # 최솟값
print("최댓값 : ", max(a, b, c))  # 최댓값
