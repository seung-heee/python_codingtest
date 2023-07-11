a = "hello"
b = "world"
# 분리시 split, 연결시 +
print(a + " " + b)

c = "String "
print(c * 3)  # 문자 반복 연결 출력 *

d = "ABCDEF"
print(d[2:4])  # 인덱스 2,3
print(d[2:])  # 인덱스 2부터 끝까지
print(d[:5])  # 처음부터 인덱스 4까지

str_length = len(d)  # 문자열 길이
str_min = min(d)  # 문자열 중 작은 값
str_max = max(d)  # 문자열 중 큰 값
str_count = d.count("B")  # 문자열 내 B의 개수

print(f"문자열 길이 {str_length}")
print(f"문자열 중 최솟값 {str_min}")
print(f"문자열 중 최댓값 {str_max}")
print(f"문자열 중 B의 개수 {str_count}")
print(d.find("C"))  # C의 위치 - 인덱스 번호
