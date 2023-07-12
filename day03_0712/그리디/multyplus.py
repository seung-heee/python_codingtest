"""
문제 : 문자열 S가 주어졌을 때 'x' 혹은 '+' 연산으로 가장 큰 수를 구하는 프로그램을 작성하세요.
모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정한다.
참고 : 각 자리가 숫자(0부터 9)로 이루어짐
"""
num = input()
num = list([int(x) for x in num])  # 정수 변경 후, list로 변환
result = num[0]  # 결과값 담을 변수

for i in num[1:]:
    if i == 0 or i == 1:
        result += i
    else:
        if result == 0:
            result += 1
        result *= i

print(result)
