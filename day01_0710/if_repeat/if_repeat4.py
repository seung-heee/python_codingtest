a = int(input("1~12사이 숫자 입력하여 월 판단 : "))
if a // 3 == 1:  # 봄: 3,4,5월
    print("spring")
elif a // 3 == 2:  # 여름 : 6,7,8월
    print("summer")
elif a // 3 == 3:  # 가을 : 9,10,11월
    print("fall")
else:  # 겨울 : 12,1,2월
    print("winter")
