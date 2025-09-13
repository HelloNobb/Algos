# 기능: 인원수-각점수들 분리저장 > 평균계산 > 평균이상 학생수계산 > 비율계산
num = []
target = []
def get_target_percent(N, aver):
    n = 0
    for i, score in enumerate(N):
        if score > aver:
            n+=1
    
    per = n/len(N) * 100
    
    return per

C = int(input())

for i in range(C):
    N = list(map(int, input().split()))
    # 원하는 데이터 가공
    num.append(N[0])	# 반별 설정된 인원수들 :num[i]
    N = N[1:num[i]+1]	# 현재 반의 점수들 : N
    ave = (sum(N) / num[i])
    target.append(get_target_percent(N,ave))

for t in target:
    print(f"{t:.3f}%")