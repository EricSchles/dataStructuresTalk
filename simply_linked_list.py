class Node:
    def __init__(self,item,next=None):
        self.item = item
        self.next = next
    def __str__(self):
        return repr(self.item)

root = Node(0)
curr = root
for i in xrange(1000):
    node = Node(i)
    curr.next = node
    curr = curr.next

curr = root
while curr != None:
    print curr
    curr = curr.next
