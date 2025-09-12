# 목표: M길이 만큼 나무 가져가기위해 설정할 수 있는 높이의 최댓값
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) #나무 수, 목표나무길이 (둘다 숫자 100만 이상)  # 5, 7
heights = list(map(int, input().split())) #나무 높이 # 10, 5, 8, 20, 9 
heights[:N].sort()


# 정답 접근방식: 이분탐색(단, 인덱스 아닌 자르는 높이를 기준으로) / 자르는높이 = 0~max(heights)
# 내 방식: 높이를 0~max의 절반이 아닌 max-M(최대높이-자르려는 목표치)로 잡음.임의값이라 언제도달할지 보장없음.
left = 0
right = max(heights)

while (left <= right):
    mid = (left+right)//2 #자를 높이
    get = 0 #수확량
    
    for h in heights:
        if h > mid:
            get += h - mid
            
    if get >= M: #조건 만족
        left = mid+1
    else:
        right = mid-1

print(right) #left아니고 right인 이유: 조건찾으면 while문 빠져나올때 left = right+1인상태됨.그전단계가답이라

# # 차이의 범위: max값-타깃값, 점점 올려보기
# target = max(heights) - M
# T = []
# while sum > M:
#     sum = 0
#     for i in N:
#         T.append(heights[i] - target)
#         sum += T[i]
#     if sum == M:
#         print("끝")
#         break
#     elif sum > M:
#         target = target + target//2
#     else:
#         target = target - target//2

    # 기저조건 어떻게?