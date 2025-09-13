#종이자르기
def get_max_length(leng, cutTargets):
    maxLen = 0
    pre = 0
    for i,cutT in enumerate(sorted(cutTargets)):
        seg = cutT-pre
        if seg > maxLen:
            maxLen = seg
        pre = cutT
    #tail check
    tail = leng-pre
    if tail > maxLen:
        maxLen = tail
    return maxLen
        

W,H = map(int, input().split())
CUT = int(input())

CW = []
CH = []
for i in range(CUT):
    WHERE,C = map(int, input().split()) #0 - width, 1 - height
    if WHERE == 0:
        CH.append(C)
    elif WHERE == 1:
        CW.append(C)
    else:
        print("[입력에러] 가로/세로는 0/1로 표현해주세요.")
## 가로 MAX길이
wMax = get_max_length(W, CW)
## 세로 MAX길이
hMax = get_max_length(H, CH)

print(wMax*hMax)