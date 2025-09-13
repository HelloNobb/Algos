T = int(input())

a = []
b = []

for i in range(T):
    x,y =map(int, input().split())
    a.append(x)
    b.append(y)

for x,y in zip(a,b):
    print(x+y)