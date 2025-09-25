import sys
from collections import deque
input = sys.stdin.readline
caseCnt = int(input().rstrip())     # 케이스 수
'''
스택을 내부적으로 관리
dictArr : 전체 노드정보(a - b 연결)
infoArr : 방문/T/F 정보
num : 시작노드
'''
def isBipartite(dictArr, infoArr, num):
    stack = []
    stack.append(num)   # num 으로 시작
    beforeNum = 0       # 부모숫자
    state = 1           # 상태값(T : 1 / F : -1)
    infoArr[num] = state
    while stack:
        print("infoArr")
        print(infoArr)
        targetNum = stack.pop()
        # infoArr[targetNum] = state
        childArr = dictArr[targetNum]   # 검사 대상 자식 가져옴
        # print(type(childArr))
        if(beforeNum in childArr):
            childArr.remove(beforeNum)  # 부모는 검사 대상 x
        # T / F 검사
        for child in childArr:
            if(infoArr[child] != 0):    # 방문한적이 있다
                if(infoArr[child] == state):        # 상태값 같으면
                    return False
            else:                       # 방문한적 없다(0이다)
                infoArr[child] = -infoArr[targetNum]
                stack.append(child)
        
    return True

for _ in range(caseCnt):
    nodeCnt, lineCnt = list(map(int, input().split()))  # 노드수, 간선수
    dictArr = {i: [] for i in range(1, nodeCnt + 1)}    # 전체 노드정보 세팅
    infoArr = [0] * (nodeCnt + 1)                       # 방문정보/T/F 체크 배열
    for _ in range(lineCnt):    # 간선 정보 입력받음
        num1, num2 = list(map(int, input().split()))
        dictArr[num1].append(num2)
        dictArr[num2].append(num1)
    flag = True     # 이분그래프가 맞냐?
    for i in range(1, len(infoArr)):
        if(infoArr[i] == 0):        # 미방문 노드면 방문
            flag = isBipartite(dictArr, infoArr, i)
    print(flag)