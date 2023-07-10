a, b = map(int, input("정수 2개를 입력받아 차를 계산 : ").split())  # map 활용한 정수 입력 방식
print(a - b)

a, b = input("정수 2개를 입력받아 차를 계산 : ").split()
c = int(a) - int(b)  # 뺄셈
d = int(a) * int(b)  # 곱셈
e = int(a) // int(b)  # 나누기
f = int(a) % int(b)  # 나머지
print(c, d, e, f)  # 사칙 연산 출력

a, b = input("단어, 반복횟수 입력 ").split()
print(a * int(b))

s = int(input("반복횟수 입력 : "))
s2 = input("문자열 직접 입력 : ")
print(s * s2)  # 문장 반복
