# 구현 _ 주민등록확인
# 주민등록번호를 입력받고, 유효한 주민등록번호인지 검증, 생년월일과 성별 출력하는 프로그램 작성하라!

# 주민등록번호 유효성 검증
birth, etc = input("주민등록번호를 입력하세요 : ").split("-")

while True:
    if len(birth + etc) == 13:  # 입력한 주민등록번호의 길이
        all = birth + etc
        total = 0
        # 주민번호 각 자리의 숫자와 가중치를 곱한 합계 계산
        for i in range(12):
            multi = int(all[i]) * (i % 8 + 2)  # 주민번호 각 자리 숫자 * 가중치
            total += multi  # 합계
            # print("{}번째 가중치를 곱한 합계 {}".format(i + 1, multi))

        # 11에서 나머지를 뺀 결과가 주민등록번호의 마지막 자리의 수와 같으면 정상, 다르면 오류
        total = (11 - total % 11) % 10
        print("올바른 주민등록번호입니다!" if int(all[12]) == total else "오류")
        print(f"주민등록번호 마지막 자리의 수 : {all[12]}, 나머지를 뺀 결과 : {total}")
        break
    else:  # 길이부터 맞지 않다면,, 입려
        print("다시 입력해주세요 :")
        birth, etc = input().split("-")


# 문자열로 입력받았으니 정수형으로 변경 후 알맞는 값 추출
year = birth[:2]  # 년
month = birth[2:4]  # 월
day = int(birth[4:6])  # 일
gender = int(etc[:1])  # 성별
city = int(etc[1:3])  # 지역

# 생년월일
if 0 <= int(year) < 24:
    print(f"생년월일 : 20{year}년 {month}월 {day}일")
else:
    print(f"생년월일 : 19{year}년 {month}월 {day}일")

# 성별
if gender % 2 == 0:
    print("여성")
else:
    print("남성")

# 거주지
if 0 <= city <= 8:
    print("서울")
elif 9 <= city <= 12:
    print("부산")
elif 13 <= city <= 15:
    print("인천")
elif 16 <= city <= 25:
    print("경기도")
else:
    print("그 외..너무 많다..")
