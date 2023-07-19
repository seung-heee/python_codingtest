from bisect import bisect_left, bisect_right


def count_by_value(bisectarray, value):
    left_index = bisect_left(array, value)
    right_index = bisect_right(array, value)
    print(left_index)
    print(right_index)

    return right_index - left_index  # 특정 값의 개수 반환


array = [1, 2, 3, 3, 3, 4, 5, 6, 7, 8]
# 특정 값을 입력받는다.
value = 3

# 특정 값의 개수를 세고 출력한다.
count = count_by_value(array, value)
print("특정 값의 개수는 {}입니다.".format(count))
