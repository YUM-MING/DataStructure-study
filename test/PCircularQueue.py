class PCircularQueue:

    def __init__(self,capacity):
        self.front = 0  # 큐에서 데이터를 빼는 위치
        self.rear = 0   # 큐에서 데이터를 넣는 위치
        self.queue = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def isEmpty(self):
        # pass
        # if self.front == self.rear:
        #     return True
        # else:
        #     return False
        # return self.front == self.rear
        return self.size == 0 # 큐에 있는 데이터 갯수

    def isFull(self):
        # pass
        # return (self.rear + 1) % self.size == self.front
        return self.size == (self.capacity - 1)

    def findHighestP(self):
        # 우선 순위가 높은 항목을 찾는 함수
        # 큐에 있는 데이터를 우선 순위로 본다.
        if self.isEmpty():
            return -1
        # else: # 문장 구조상 안 써도 된다.
        highest = 0
        for i in range(1,self.size):
            if self.queue[highest] < self.queue[i]:
                highest = i
        return highest
            

    def enqueue(self, data):
        # pass
        # queue가 full이 아니면 동작
        # rear = rear + 1 <- 스택
        if not self.isFull():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        highest = self.findHighestP()
        if highest == -1: # empty
            return None
        # 우선 순위가 높은 데이터 위치를 찾았다.
        # highest
        # highest번째 데이터를 그냥 빼면 안된다
        # 큐의 중간에 빈자리가 생기기 때문에..
        # highest번째 데이터를 맨 앞(front)
        # highest번째 데이터를 맨 뒤(rear(환형)), size(환형))
        self.front += (self.front + 1) % self.capacity
        self.queue[highest], self.queue[self.front] = \
            self.queue[self.front], self.queue[highest]
        return self.queue[self.front]
        # if not self.isEmpty():
        #     self.front = (self.front + 1) % self.size
        # return self.queue[self.front]
    
    def peek(self):
        if not self.isEmpty():
            return self.queue[self.front]
        
if __name__ =="__main__" :
    cqueue = PCircularQueue(10)