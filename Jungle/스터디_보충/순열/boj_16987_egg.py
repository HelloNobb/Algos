'''
[계란으로 계란치기]:~9:20 

# 문제 조건 ====
- 각 계란 - 내구도, 무게
* 계란으로 계란을 치게 되면 각 계란의 내구도는 상대 계란의 무게만큼 깎이게 된다. 
* 내구도가 0 이하가 되는 순간 계란은 깨지게 된다

1. 가장 왼쪽의 계란을 든다.
2. 손에 들고 있는 계란으로 깨지지 않은 다른 계란 중에서 하나를 친다. 
	단, 손에 든 계란이 깨졌거나 깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다. 
	이후 손에 든 계란을 원래 자리에 내려놓고 3번 과정을 진행한다.
3. 가장 최근에 든 계란의 한 칸 오른쪽 계란을 손에 들고 2번 과정을 다시 진행한다. 
	단, 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우 계란을 치는 과정을 종료한다.
 
> 최대 몇 개의 계란을 깰 수 있는지?

# input ====
N (계란 개수)
(N줄로 계란 내구도 무게 정보)


# 접근 전략 ====
/ 왼쪽부터 하나씩 다른 계란을 침.(n-1회)
/ 만약 현재 차례 계란 깨져있거나 나머지 계란들 다 깨져있으면 패스 (+가장 마지막 계란은 패스)
/ 최대로 많이 깨야함

> 


1) n-1개중에서 하나 뽑기 (자기차례에 자기자신 제외) * 전체계란 반복
2) 깨기
3) 조건 확인 -> 전체 (n-1)회 돌릴때마다 깨진 계란 개수 세서 max보다 크면 max 갱신

def hit_result(egg1, egg2)
	- 계란치기 이후 각 2개 계란의 내구도 반환
 
def choose_and_hit() #dfs > 순열 뽑기

'''
import sys
input = sys.stdin.readline

EGGS = []
# 입력 ====
N = int(input())
for i in range(N):
    d, w = list(map(int, input().split()))
    EGGS.append([d, w]) # (내구도, 무게)

# dfs(b-tracking) - idx: 0~N-1 / i: 나 제외+이미깨진거 제외 하나 ====
MAX_BROKEN_COUNT = 0

def choose_and_hit(idx): #idx = 뽑은 것
    global MAX_BROKEN_COUNT
    
    if idx == N:
        # max_brok_count 업데이트
        broken = 0
        for d,w in EGGS:
            if d <= 0:
                broken += 1
        if MAX_BROKEN_COUNT < broken:
            MAX_BROKEN_COUNT = broken
        return
    
    # self-check 
    if (EGGS[idx][0] <= 0):
        choose_and_hit(idx+1)
        return
    
    hit_possible = False #나는 살아있는데 나머지 다 깨진 경우 감지
    
    for i in range(N):
        # 지금 손에 든 계란이 이ㅣ ㄲ재여 ====
        if (i == idx or EGGS[i][0] <= 0): #뽑은 게 자기자신 / 내구도<=0 이면 패스
            continue
            
        hit_possible = True
        # hit ====
        EGGS[idx][0] -= EGGS[i][1]
        EGGS[i][0] -= EGGS[idx][1]
        
        # 백트래킹 ====
        choose_and_hit(idx+1) #다음 계란으로
        
        # 내구도 원상복귀 ====
        EGGS[idx][0] += EGGS[i][1]
        EGGS[i][0] += EGGS[idx][1]
    
    if not hit_possible:
        choose_and_hit(idx+1)
    
choose_and_hit(0)
print(MAX_BROKEN_COUNT)
