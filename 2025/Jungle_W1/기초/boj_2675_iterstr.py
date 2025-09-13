T = int(input()) #case no

N = [] #케이스별 반복횟수
S = [] #케이스별 통문자열들


arr = [input() for t in range(T)] # 일단 케이스수만큼 통문자열받기

for i in range(T):
    no = int(arr[i].split()[0])
    st = arr[i].split(' ',1)[1]
    
    N.append(int(no)) #3 5 2 (repeat amounts)
    S.append(st) #khj jkd a1df (repeat targets)
    
for j in range(T):
    for s in S[j]:
        for l in range(N[j]):
            print(s,end="")
    print()