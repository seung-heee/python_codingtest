from bisect import bisect_left, bisect_right

N = int(input("전자매장에 있는 부품 개수 : "))
N_lst = []

for i in range(N):
    num = int(input("부품의 고유한 번호 : "))
    N_lst.append(num)
    N_lst.sort()

M = int(input("손님이 찾는 종류 : "))
M_lst = []

for i in range(N):
    num = int(input("손님이 찾는 부품의 번호 : "))
    M_lst.append(num)
    M_lst.sort()


def count_by_value(bisectarray, value):
    left_index = bisect_left(N_lst, value)
    right_index = bisect_right(N_lst, value)
    return right_index - left_index  # 특정 값의 개수 반환


# 특정 값을 입력받는다.
value = 3

# 특정 값의 개수를 세고 출력한다.
count = count_by_value(N_lst, value)
print("특정 값의 개수는 {}입니다.".format(count))
