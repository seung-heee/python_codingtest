from collections import deque # 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print(queue)
queue.popleft()
print(queue)

queue.append(9)
queue.append(7)
queue.append(6)
queue.popleft()

queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력