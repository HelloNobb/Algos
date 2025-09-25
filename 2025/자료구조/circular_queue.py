class CircularQueue:
    def __init__(self, cap):  #cap: 설정한 배열길이
        self.capacity = cap+1
        self.Q = [None] * self.cap
        self.front = 0
        self.rear = 0
    def is_empty(self):
        return self.front == self.rear
    def is_full(self):
        return (self.rear+1) % self.capacity == self.front
    def enqueue(self, x):
        if self.is_full():
            return
        self.rear = (self.rear + 1) % self.cap
        self.queue[self.rear] = x
    def dequeue(self):
        if self.is_empty():
            return
        self.front = (self.front + 1) % self.cap
        return self.queue[self.front]    ## front: 바로직전인덱스라,업뎃한게 이전front의인덱스임