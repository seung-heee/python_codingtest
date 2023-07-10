print("첫번째 정수 a를 입력해주세요 : ", end="")
a = input()
print("두번째 정수 b를 입력해주세요 : ", end="")
b = input()
print(f"a : {a}, b : {b}")

print("한번에 문자 c, d를 입력받습니다 :", end="")
# 문자 2개 입력, 공백 기준 분리
# 정수형 map(int, input.split())
# 실수형 map(float, input.split())
c, d = input().split()
print(f"c : {c}, d: {d}")
