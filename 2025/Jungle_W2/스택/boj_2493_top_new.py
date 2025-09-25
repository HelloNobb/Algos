import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    T = list(map(int, input().split()))
    
    stack = [] #(높이-인덱스) 저장 >> 접근시, stack[인덱스]: (높이,인덱스) / stack[쌍의 인덱스][0]:높이 / stack[쌍의인덱스][1]:인덱스
    result = [0]*N #답 저장(각 탑 별 레이저받이 탑 번호)
    
    #left->right 탑 순회
    for i in range(N):
        height = T[i] #이번 타워높이
        
        while stack and stack[-1][0] <= height: #스택존재안하거나 가장가까운탑높이가 현재타워높이보다 높을때까지
            stack.pop()	# 삭제
        if stack:
            result[i] = stack[-1][1]+1
        
        stack.append((height, i))
        
    print(*result)
    
solve()