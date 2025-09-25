import sys
input = sys.stdin.readline
from collections import deque
############### 로직은 맞으나 비효율적이고 시간초과(TLE) 발생한 코드 ========
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
        return self.data[-1]
        
    def size(self):
        return len(self.data)
    
    def empty(self):
        return not self.data
    
    def is_empty(self):
        return len(self.data) == 0

    
def get_received_top(T, idx): #애초에 받을때 잘라서주기(~기준탑) [6,9,5]**반대로받아야함
    st = Stack()
    for x in T[:idx+1]: #6 >9 >5
        st.push(x)
    sender = st.pop()
    #sys.stdout.write(f"sender: {sender}\n")
    #st.pop() #제일 마지막 탑이 기준 / 5
    while not st.is_empty():
        receiver = st.pop()
        if receiver >= sender:
            #sys.stdout.write(f"목표 수신자 확보: {receiver}\n")
            return receiver
        #sys.stdout.write(f"{receiver} 지나가는중\n")
    return 0

N = int(input())
T = list(map(int, input().split()))
r_num = []
for i in range(N):
    r_top = get_received_top(T[:len(T)-i], len(T)-i)
    if r_top == 0:
        #print(0, end=" ")
        r_num.append(0)
    else:
        r_idx = T.index(r_top)
        #print(r_idx+1, end=" ")
        r_num.append(r_idx + 1) #인덱스(0~) 아닌 번호(1~) 출력해야해서

r_num = reversed(r_num)
print(*r_num)

### 시간초과 원인 ==========
'''
	1- 리스트 슬라이싱 반복 ([:len(T)-i])
		> 매번 슬라이싱할때마다 O(n) --> for문 내에 슬라이싱 => O(n^2)

	2- arr.index() : 리스트의 처음부터 값을 찾을때까지 순차 탐색함 >> 최악의 경우O(n)
 
	3- get_reveieved_top() 함수 반복탐색  :  O(N)
'''