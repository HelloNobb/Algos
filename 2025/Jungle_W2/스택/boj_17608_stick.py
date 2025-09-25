import sys
input = sys.stdin.readline
from collections import deque

class StickStack:
    def __init__(self):
        self.data = deque()
    def push(self, x):
        self.data.append(x)
    def pop(self):
        self.data.pop()
    def size(self):
        return len(self.data)

       
def add_stick(A):
    st = StickStack()
    
    pre_stick = A[len(A)-1]
    st.push(pre_stick)
    for i in range(len(A)-2, -1, -1):
        current_stick = A[i]
        if current_stick <= pre_stick:
            continue
        else:
            st.push(current_stick)
            pre_stick = current_stick
    return st.size()
    
N = int(input())
S = [int(input()) for i in range(N)]
print(add_stick(S))