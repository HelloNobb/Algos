## 재귀: 1000회 호출이내에만 가능. 그 이상이면 반복문 사용해야함

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
# cards = deque()
# for i in range(N,0,-1):
#     cards.append(i)
# ======= >> 위 코드를 아래 한문장으로 가능!
cards = deque(range(N,0,-1))

def get_last(C):
    while len(C) > 1:
        C.pop() #뒤에서 꺼내서 버리기
        C.appendleft(C.pop()) #뒤에서 꺼내서 앞에다 집어넣기
    return print(C.pop())

get_last(cards)