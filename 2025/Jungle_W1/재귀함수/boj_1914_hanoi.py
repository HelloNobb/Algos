# hanoi : T(n) = T(n-1)*2 + 1
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def hanoi(n, start, end, via, out):
    if n == 1:
        #print(start, end)
        out.append(f"{start} {end}\n")
        return
    hanoi(n-1, start, via, end,out) #n-1개 이동 (via=2로)
    #print(start, end) #n번째 이동 (end=3로)
    out.append(f"{start} {end}\n")
    hanoi(n-1, via, end, start,out) #n-1 (end=3로)
        

N = int(input())
print(2**N -1)

if N <= 20:
    out = []
    hanoi(N,1,3,2,out)
    sys.stdout.writelines(out)

##  ------ 팀코어회의
## 일일히 변수로 만들지않고
# def move(num, start, target)
# def move(num-1, start, target-)
# 점화식:  a<n+1> = 2 * a<n>  + 1