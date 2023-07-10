a = input("문자열 1개 입력 : ")
print(a, 3 * ("\n"))  # a입력, 줄바꿈 3줄
print(a, a, a)  # a를 연속 3번 출력

b, c = input("문자를 2개 입력해주세요:").split()
print(b + c + "\n")
print(b + "\n" + c)

d, e = input("문자 2개를 입력해주세요, 콤마 구분 :").split(",")
print(d, e)

# 문자 2개 입력, 콤마로 구분, 최대 분리 횟수 1회로 제한
f, g = input("문자 2개를 입력해주세요, 콤마 구분, 1개 제한 : ").split(",", 1)
print(f, g, sep=":")
