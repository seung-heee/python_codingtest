"""
문제 : 문자열 S가 주어졌을 때 'x' 혹은 '+' 연산으로 가장 큰 수를 구하는 프로그램을 작성하세요.
모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정한다.
참고 : 각 자리가 숫자(0부터 9)로 이루어짐
"""
num = input()
num = list([int(x) for x in num])  # 정수 변경 후, list로 변환
print(num)
count = 0  # 1담을 변수
result = 1  # 결과값 담을 변수

for i in num:
    if i == 0:
        continue
    elif i == 1:
        count += 1
    else:
        result *= i
result += count
print(result)
