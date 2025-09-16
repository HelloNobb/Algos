from collections import deque
import sys
input = sys.stdin.readline ## 각문자단위로 받고싶을땐 rstrip로 개행문자('\n') 꼭 없애기!!

class Stack:
    def __init__(self):
        self.stack = deque()
    
    def push(self, x):
        self.stack.append(x)
        
    def pop(self):
        if self.is_empty():
            return False
        self.stack.pop() #마지막 원소 삭제
        return True

    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

#st = Stack() ==> 여러 배열을 다 여기다 만들어쓰면 다음 케이스검사때 영향줌!(매번 새롭게 생성해야함)

def check_gwalho(G): #끝났는데 빔->O / 끝났는데 남음->X / empty일때 pop->X
    st = Stack()
    
    for g in G:
        if g == "(":
            st.push(g)
        else: #")"
            if not st.pop():
                print("NO")
                return
            
    if st.is_empty():
        print("YES")
    else:
        print("NO")

T = int(input())
A = [list(input().rstrip()) for i in range(T)]
for i in range(T):
    check_gwalho(A[i])