# 주민등록번호 문자열을 입력 받아 숫자만 출력하시오
s = input().split("-")  # 문자열 -을 기준으로 분리되어 리스트 반환
print("".join(s))  # 공백으로 문자열 병합

# -으로 분리하여 입력받은 후 공백으로 문자열 바로 병합해줌
print("".join(input("주민등록번호 입력해주세요, 구분자 - : ").split("-")))  # 한줄로 표현...
