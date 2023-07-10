data = input("문자를 입력해주세요 .으로 구분 : ").split(".")
print("-".join(data))  # 문자 -로 연결 출력
data.reverse()  # 구분된 문자열 열 뒤집기(정렬X)
print(":".join(data))  # 문자 :로 연결 출력
print(data)
print(data[0], data[1])  # 구분된 문자의 내부 인덱스 번호로 출력
