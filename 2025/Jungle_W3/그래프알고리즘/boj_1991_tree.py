N = int(input())

TREE={}
for i in range(N):
    parent,left,right = input().split()
    TREE[parent] = (left, right)
    
#전위
def preorder(node):
    if node == '.':
        return
    global TREE
    l, r = TREE[node]
    
    print(node, end='')
    preorder(l)
    preorder(r)
#중위
def inorder(node):
    if node == '.':
        return
    global TREE
    l, r = TREE[node]
    
    inorder(l)
    print(node, end='')
    inorder(r)
#후위
def postorder(node):
    if node == '.':
        return
    global TREE
    l, r = TREE[node]
    
    postorder(l)
    postorder(r)
    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()