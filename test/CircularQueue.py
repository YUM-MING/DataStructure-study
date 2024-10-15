class CircularQueue:

    def __init__(self,size):
        self.front = 0  # 큐에서 데이터를 빼는 위치
        self.rear = 0   # 큐에서 데이터를 넣는 위치
        self.queue = [None] * size
        self.size = size

    def isEmpty(self):
        # pass
        # if self.front == self.rear:
        #     return True
        # else:
        #     return False
        return self.front == self.rear

    def isFull(self):
        # pass
        return (self.rear + 1) % self.size == self.rear
    
    def enqueue(self, data):
        # pass
        # queue가 full이 아니면 동작
        # rear = rear + 1 <- 스택
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.size
        return self.queue[self.front]
    
    def peek(self):
        if not self.isEmpty():
            return self.queue[self.front]
        
if __name__ =="__main__" :
    cqueue = CircularQueue(10)