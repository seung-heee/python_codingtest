c = ord(input("A부터 입력한 문자까지 순서대로 출력 : "))
i = ord("a")  # a의 아스키코드 정수 값 65

while i <= c:
    print(chr(i), end=" ")
    print(i, end=" ")
    i += 1
