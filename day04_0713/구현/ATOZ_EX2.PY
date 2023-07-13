real_lst = [chr(i) for i in range(ord("a"), ord("z") + 1)]
clear_lst = [-1 for i in range(ord("a"), ord("z") + 1)]

s = "ohmygd"
s = list(s)

for lst in real_lst:  # a~z 리스트 돌리고
    for word in s:  # 입력받은 단어 돌리고
        if word == lst:
            print(word)
            new = real_lst.index(word)
            clear_lst[new] = "fuck.."

print(clear_lst)
