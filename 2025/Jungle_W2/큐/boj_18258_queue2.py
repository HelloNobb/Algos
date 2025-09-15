import sys
input = sys.stdin.readline
from collections import deque
class Queue:
    def __init__(self):
        self.data = deque()
    
    def push(self, x): # push(v) 이렇게만 불러도 자동 첫 인자 self<-st 넣어줌
        self.data.append(x)
  
    def pop(self):
        if self.empty():
            return -1
        return self.data.popleft()
    
    def front(self):
        if self.empty():
            return -1
        return self.data[0]
    def back(self):
        if self.empty():
            return -1
        return self.data[-1]
    
    def empty(self):
        if len(self.data) == 0:
            return 1
        return 0
    
    def size(self):
        return len(self.data)

q = Queue()
N = int(input())
for i in range(N):
	cmd = input().split()
	if cmd[0] == "push":
		v = cmd[1]
		q.push(v)
	elif cmd[0] == "front":
		print(q.front())
	elif cmd[0] == "pop":
		print(q.pop())
	elif cmd[0] == "empty":
		print(q.empty())
	elif cmd[0] == "back":
		print(q.back())
	else:
		print(q.size())