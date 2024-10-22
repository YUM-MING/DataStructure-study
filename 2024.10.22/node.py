class Node:
    def __init__(self):
        self.data = None
        self.link = None
        # 두 개의 속성을 갖는 클래스

    def __str__(self):
        return f"객체의 속성 중 data는 {self.data}이다"
    
    def __add__(self, node):
        self.data = self.data + node.data
        return self
