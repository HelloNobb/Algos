# hanoi top	> 개수만큼 A->C로 옮기기
def get_hanoi(n):
    if n == 1:
        return 1
    else:
        return 2*get_hanoi(n-1) + 1

def hanoi(n, start, spare, end):
    if n == 1:
        print(start, end)
        return
    hanoi(n-1, start, end, spare)
    print(start, end)
	
        
        

N = int(input())
print(get_hanoi(N))


##  ------ 팀코어회의
## 일일히 변수로 만들지않고
# def move(num, start, target)
# def move(num-1, start, target-)
# 점화식:  a<n+1> = 2 * a<n>  + 1