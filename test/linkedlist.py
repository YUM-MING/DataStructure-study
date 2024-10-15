from Node import Node # from 파일명 import 함수

head1 = None
# head2 = Node() 금지
node1 = Node()
node2 = Node()

print(node1)
print(node2)
node1.next = node2
head1 = node1
node1.data = 20
node1.next = node2
node2.data = 30

print(head1)
print("node1의 속성 data는 ", node1.data)
print("node1의 속성 data는 ", head1.data)
print("node3의 속성 data는 ", head1.next.data)

head2.next = node1
node1.next = node2
print(head2.next.data)
print(head2.next.next.data)