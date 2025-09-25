'''
# 이분 그래프
 - visited = [0]*N
 - 
 # 접근방법
0-1. 노드 크기만큼의 배열에 전부 0을 넣음 (색칠: 1/-1 , 아직색칠안함: 0)
0-2. 각 노드 인덱스를 딕셔너리 키로 만들고 값에 연결된 애들을 모두 넣는다.
1. 아무거나부터 시작_ 1번에서 시작> color[1] = 1로 색칠 (연결돼있는애들은 -1 색칠 예정)
  > 연결된 애들 쭉 확인해 0->(자신의반대색인)-1 설정/ -1->무시 / 1->바로 False처리하고 탐색종료
2.
'''
import sys
from collections import deque
import pprint
#K = int(input())

def color_nodes(GRAPH, V):
    color = [0]*(V+1)
    
    for i in range(1, V+1): #중복되지않게 다 체크하기위함
        if color[i] != 0:
            continue #이미 색칠한거란 뜻은 걔 연결된애들 이미 다 색칠돼있단 뜻,통과란뜻
        
        color[i] = 1
        stack = deque()
        stack.append(i)
        
        children = list(GRAPH[i])
        for c in children:
            stack.append(c) 
            
        while stack:
            now = stack.pop()
            for child in GRAPH[now]:
                if color[child] == 0:
                    color[child] = -color[i]
                    stack.append(child)
                elif color[child] == color[i]:
                    return False
             
    return True


##====inputs / V:정점, E:간선
K = int(input())
V,E = map(int, input().split())

GRAPH = {i: [] for i in range(1,V+1)}

for i in range(E):
    node1,node2 = map(int, input().split())
    GRAPH[node1].append(node2)
    GRAPH[node2].append(node1)

print(color_nodes(GRAPH, V))

#pprint.pprint(GRAPH)