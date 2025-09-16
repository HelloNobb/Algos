from collections import deque
import sys
input = sys.stdin.readline

class Stack:
	def __init__(self):
		self.data = deque()

	def push(self, x):
		self.data.append(x)
  
	def pop(self):
		if self.is_empty():
			return -1
		return self.data.pop()

	def top(self):
		if self.is_empty():
			return -1
		return self.data[-1]
  
	def is_empty(self):
		if len(self.data) == 0:
			return 1
		return 0
	
	def size(self):
		return len(self.data)
	
	def sum(self):
		sum = 0
		for d in self.data:
			sum += d
		return sum

st = Stack()
K = int(input())
for i in range(K):
    x = int(input())
    if x == 0:
        st.pop()
    else:
        st.push(x)

print(st.sum())
