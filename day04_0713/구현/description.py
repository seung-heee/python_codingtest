s = "hegellogo nigicege dagay"  # input() 입력받는 값
aeiou = ["a", "e", "i", "o", "u"]
result_s = []
idx = 0

while idx < len(s):
    result_s.append(s[idx])  # 리스트에 문자열 추가
    if s[idx] in aeiou:  # 문자열이 모음을 만나면
        idx += 2  # 인덱스 2칸 건너뛰기
    idx += 1  # 인덱스 값 증가

print("".join(result_s))  # 리스트를 문자열로 변경 후 출력!!!!
