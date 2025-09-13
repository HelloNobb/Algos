#달팽이: V미터 목표, 낮 +A미터, 밤 -B미터	/ 1<=B < A <= V <= 백만 // 며칠걸리겠나?
## 시간초과 코드 (로직은 틀리지 않음)
#A,B,V = map(int, input().split())

# count = 0
# while V > 0:
#     count+=1
#     V -= A
#     if (V <= 0):
#         break
#     V += B

# print(count)
## =======================챗지피티 도움
#### 문제: 올림/내림처리
# V-A 지점까지 8.XX일이 걸린다면, 실질적으로 9 + 1 = 10일 필요
# V-A 지점까지 정확히 8일이 걸린다면, 실질적으로도 8 + 1 = 9일 필요
# 오답 - day = (V-A)//(A-B) + 1 # >> 무조건 내림이 되어 잘못됨
# 정답 - 내림이 아닌 무조건올림을 해줘야함(정수인경우만빼고 모두 올려줌 = 'math.ceil(x)')
import math
A,B,V = map(int, input().split())
day = math.ceil((V-A)/(A-B)) + 1
print(day)