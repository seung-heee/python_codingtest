from bisect import bisect_left, bisect_right


def count_by_value(bisectarray, value):
    left_index = bisect_left(lst1, value)
    right_index = bisect_right(lst1, value)
    print(left_index)
    print(right_index)
    return right_index - left_index  # 특정 값의 개수 반환


lst1 = [2, 3, 3, 5, 7, 8, 9]
lst2 = [2, 3, 5]
# 특정 값을 입력받는다.
value = 3

# 특정 값의 개수를 세고 출력한다.
count = count_by_value(lst1, value)
print("특정 값의 개수는 {}입니다.".format(count))
