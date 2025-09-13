#selected sol: binary search
import sys
input = sys.stdin.readline

def bin_search(ARR, t):
    li = 0
    ri = len(ARR) - 1
    
    while li <= ri:
        mi = (li + ri) // 2
        if t == ARR[mi]:
           return 1
        elif t < ARR[mi]:
            ri = mi - 1
        else:
            li = mi + 1
        
        if li > ri:
            return 0


N = int(input()) #array elements amount
A = list(map(int, input().split()))
A.sort()
M = int(input()) #targets amount
B = list(map(int, input().split()))

for i in range(M):
    print(bin_search(A, B[i]))