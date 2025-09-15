# 스택 구현
import sys
input = sys.stdin.readline
class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, x): # push(v) 이렇게만 불러도 자동 첫 인자 self<-st 넣어줌
        self.data.append(x)
  
    def pop(self):
        if self.empty():
            return -1
        return self.data.pop()
    
    def top(self):
        if self.empty():
            return -1
        return self.data[-1]
    
    def empty(self):
        if len(self.data) == 0:
            return 1
        return 0
    
    def size(self):
        return len(self.data)
    
st = Stack() #instance
N  = int(input())

# 1_ 한문장씩 커맨드 올라올때마다 진행과정 출력 방법 ====
for i in range(N):
	cmd = input().split()
	if cmd[0] == "push":
		v = cmd[1]
		st.push(v)
	elif cmd[0] == "top":
		print(st.top())
	elif cmd[0] == "pop":
		print(st.pop())
	elif cmd[0] == "empty":
		print(st.empty())
	else:
		print(st.size())
  
# 2_ 명령어 매핑 >> 입력 끝날때까지 쌓아뒀다가 한번에 진행과정 출력 ====
out = []
actions = {
	"pop": lambda: out.append(str(st.pop())),
	"top": lambda: out.append(str(st.top())),
	"size": lambda: out.append(str(st.size)),
	"empty": lambda: out.append(str(st.empty()))
}

for i in range(N):
    cmd = input().split()
    if cmd[0] == "push":
        st.push(cmd[1])
    else:
        actions[cmd[0]]()

for o in out:
    sys.stdout.write("\n".join(o))