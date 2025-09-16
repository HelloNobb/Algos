import sys
input = sys.stdin.readline

class MaxHeap:
    def __init__(self):
        self.data = []
    
    def push(self, x):
        # 맨 끝에 삽입
        self.data.append(x)
        idx = len(self.data) - 1
        # 부모와 비교해 버블업
        while idx>0:
            parent = (idx - 1 )// 2
            if self.data[parent] < self.data[idx]:
                self.data[parent], self.data[idx] = self.data[idx], self.data[parent]
                idx=parent
            else:
                break
    
    def pop(self):
        if not self.data:
            print("0")
            return None
        if len(self.data) == 1:
            print(self.data[0])
            return self.data.pop()
        #루트 꺼내고
        root = self.data[0]
        print(root) ###
        # 마지막 원소를 루트로 이동 (끝원소 팝 시켜서 data[0]인 루트노드에 집어넣음)
        self.data[0] = self.data.pop()
        idx=0
        #자식과 비교해 버블다운
        while True:
            left = 2*idx + 1
            right = 2*idx + 2
            maxy = idx
            
            if left < len(self.data) and self.data[left] > self.data[maxy]:
                maxy = left
            if right < len(self.data) and self.data[right] > self.data[maxy]:
                maxy = right
            
            if maxy != idx:
                self.data[idx], self.data[maxy] = self.data[maxy], self.data[idx]
                idx = maxy
            else:
                break
        return root
h = MaxHeap()

N = int(input())

for i in range(N):
    x = int(input())
    if x > 0:
        h.push(x)
    elif x == 0:
        h.pop()
    else:
        break
