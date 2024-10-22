from node import Node

node = Node()
node.data = 10

# node3 = node + node2
print(node)
## 연산자 중복 __add__
##            __str__
node2 = Node()
node2.data = 20
node3 = node + node2
print(node3)