# 한수 : 각 자리가 등차수열 이루는 자연수
##### 잘못된점: 1의자리랑 100의자리만으로는 주어진수의 범위를 구할수없음 간과

def is_hansu(n):
    no3 = n // 100
    no2 = n // 10 % 10
    no1 = n % 10
    
    if no3-no2 == no2-no1:
        return True
    else:
        return False


N = int(input())
if N <= 99:
    ANSWER = N
elif N < 111:
    ANSWER =99
elif N == 1000:
    ANSWER = 99 + 5*9
else:
    count=0
    for i in range(N,100,-1):
        if is_hansu(i):
            count+=1
    ANSWER = count + 99
print(ANSWER)