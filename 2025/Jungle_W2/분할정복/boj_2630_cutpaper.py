N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)] ##2차원배열로 입력받기

white = blue = 0

def cut_paper(A): #행렬
    global white, blue
    
    first = A[0][0]
    if all(x == first for row in A for x in row):
        if first == 1:
            blue += 1
        else:
            white += 1
        return
    
    row = len(A) // 2
    col = len(A[0]) // 2
    # m1 = A[:row, :col] #numpy ver
    # m2 = A[:row, col:]
    # m3 = A[row:, :col]
    # m4 = A[row:, col:]
    m1 = [r[:col] for r in A[:row]] #row행의 col행
    m2 = [r[col:] for r in A[:row]]
    m3 = [r[:col] for r in A[row:]]
    m4 = [r[col:] for r in A[row:]]
    check_box(m1)
    check_box(m2)
    check_box(m3)
    check_box(m4)
    
    
    
def check_box(M):
    global white, blue
    # if np.all(M == M[0,0]): #numpy ver
    #     if M[0,0] == 1:
    first = M[0][0]
    if all(x == first for row in M for x in row):
        if first == 1:
            blue += 1
        else:
            white += 1
    else:
        cut_paper(M)

cut_paper(paper)
print(white)
print(blue)