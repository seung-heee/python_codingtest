# 변환과 연산자
n = int(input("10진수 입력 : "))
print("10진수 -> 문자 : ", chr(n))  # 10진수 -> 문자

print(ord(input("문자 -> 아스키코드(a~z 입력) : ")))  # 문자 -> 아스키코드

print("%x" % int(input("10진수 -> 유니코드 : ")))
print("%x".upper() % int(input("10진수 -> 유니코드 대문자 : ")))  # 10진 정수 --> 유니코드(대문자)

f = int(input("정수의 부호를 변환 : "))
print(-f)  # 부호 변환 출력

c = input("문자 -> 아스키코드 -> 아스키코드 +1 값 출력 : ")
c2 = ord(c)  # 아스키 코드 값을 1 증가
c3 = ord(c) + 1
print(c2)  # 10진 정수
print(c3)  # 10진 정수
print(chr(c2))  # 10진 정수 -> 문자 출력
print(chr(c3))  # 10진 정수 -> 문자 출력
