pt = 1

N = int(input())
A = [input().strip() for _ in range(N)]	#strip: 문자열 앞뒤 공백,\n,탭 삭제후 반환

S = []
for i in range(N):
    S.append(0)
    acc = 0     #누적개수
    for a in A[i]:
        if a == 'O':
            S[i] += (pt + acc)
            acc += 1
        else:
            acc = 0
    
for i in range(N):
    print(S[i])