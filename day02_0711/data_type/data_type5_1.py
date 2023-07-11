# 자료형
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # 튜플, 소괄호로 선언 및 초기화
this_is_not_tuple = "Seoul"
print(type(this_is_not_tuple))  # 튜플 nope! 문자열임. str

this_is_tuple = ("Seoul",)  # 콤마를 최소 1개 이상 추가 필요
print(type(this_is_tuple))  # 튜플임!

print(a[3])  # 4
print(a[1:4])  # 2,3,4
print(a[:])  # 전체 출력
print(type(a))

b = (1, "apple", "banana", 3.13, [1, 2, 3, 4, 5])  # 서로 다른 데이터, 자료구조 입력
c = tuple(range(1, 10))  # range 함수로 초기화 가능
print(b)

for c_tuple in c:
    print(c_tuple)
print(c)
