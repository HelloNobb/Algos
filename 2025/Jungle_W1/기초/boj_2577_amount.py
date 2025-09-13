N = [int(input()) for _ in range(3)]

total = 1
for n in N:
    total *= n

nums = list(map(int, str(total)))
targets = [0,0,0,0,0,0,0,0,0,0]

for i in str(total):
    targets[int(i)] += 1	##learned
    
[print(t) for t in targets]