class Node:
    def __init__(self, data): #생성자 (객체 생성하자마자 호출됨)
        self.data = data
        self.next = None #다음 노드객체 가리키는 참조변수
        
class LinkedList:
    def __init__(self):
        self.head = None #start node
    
    def append(self, value):	#맨 뒤에 삽입
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        
        while current_node.next:    # 다음 노드 없을때까지
            current_node = current_node.next #마지막 노드가 담길 예정
            
        current_node.next = new_node #마지막 노드의 다음노드로 등록
    
    def insert_front(self, value):		# 맨 앞에 삽입
        new_node = Node(value)
        
        new_node.next = self.head	# 원래 헤드 노드를 새 노드의 next에 넣기
        self.head = new_node	# 새 노드를 헤드로 설정
        
        
    def insert_after(self, target, data):	#특정 값 뒤에 삽입
        current_node = self.head
        
        while current_node and current_node.data != target:	#현재노드 객체가 없거나, 현재노드의 데이터가 타깃일때까지
            current_node = current_node.next
            
        if current_node:
            # next 링크 수정 작업
            new_node = Node(data)	#새로 노드 만들어
            new_node.next = current_node.next	#새 노드의 next<- 타깃노드의 next
            current_node.next = new_node	#타깃노드의 next<- 새 노드
        
        
    def delete(self, data):	#특정 값 삭제
        current_node = self.head
        if not current_node:
            return
        if current_node.data == data:	#첫째원소는 따로 판별 (다음 노드에 head 넘겨주면 그만)
            self.head = current_node.next
            return
        
        pre_node = None	#삭제할 노드의 앞 노드 담아두는 용 (링크변경목적)
        while current_node and current_node.data != data:
            pre_node = current_node
            current_node = current_node.next
        if current_node:	#찾으면
            pre_node.next = current_node.next
    
    
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


ll = LinkedList()
ll.append(2)
ll.append(5)
ll.append(0)
ll.delete(2)
ll.display()