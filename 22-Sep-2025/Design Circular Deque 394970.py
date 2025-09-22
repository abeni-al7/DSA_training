# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.k = k
        self.head = self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.size == self.k:
            return False

        elem = Node(value)

        if not self.tail:
            self.tail = self.head = elem
        else:
            self.head.prev = elem
            elem.next = self.head
            self.head = elem
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.k:
            return False
        
        elem = Node(value)
        if not self.tail:
            self.head = self.tail = elem
        else:
            elem.prev = self.tail
            self.tail.next = elem
            self.tail = elem
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        elif self.size == 1:
            self.head = self.tail = None
        else:
            next_node = self.head.next
            next_node.prev = None
            self.head = next_node
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        elif self.size == 1:
            self.head = self.tail = None
        else:
            prev_node = self.tail.prev
            prev_node.next = None
            self.tail = prev_node
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.size == 0:
            return -1
        return self.head.val

    def getRear(self) -> int:
        if self.size == 0:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

# deq = [1, 3, 4]