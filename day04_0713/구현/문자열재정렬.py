s = input()
s = list(s)

value = 0  # 숫자 담을 변수
result = []  # 문자 담을 리스트

for i in s:  # 입력받은 값 반복
    if i.isalpha():  # 문자열이면
        result.append(i)  # 리스트에
    else:  # 숫자면
        value += int(i)  # 정수형으로 변환해서 더함

result.sort()  # 문자열 정렬
result.append(str(value))  # 더한 값을 문자열 변환 후 result에 담기
print("".join(result))  # 리스트를 문자열로 연결.
