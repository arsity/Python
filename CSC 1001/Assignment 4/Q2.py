class Node:
    def __init__(self, element: int, pointer):
        self.element = element
        self.pointer = pointer


class SinglyLinkedList:
    def __init__(self):
        self.head = Node(56, None)
        self.tail = self.head
        self.head = Node(48, self.head)

    def insert(self, data: str):
        self.head = Node(data, self.head)

    def recursive_count(self, node: Node):
        if node.pointer == None:
            return 1
        else:
            return 1 + self.recursive_count(node.pointer)

    def quick_sort(self):
        self.__compare(self, nowNode=self.head, startNode=self.head,
                       endNode=self.tail, pivot=self.head)

    def __compare(self, nowNode: Node, startNode: Node, endNode: Node, pivot: Node):
        if startNode != endNode:
            if nowNode.pointer != endNode.pointer:
                self.__compare(nowNode=nowNode.pointer,
                               startNode=startNode, endNode=endNode, pivot=pivot)
            if nowNode.element < pivot.element:
                nowNode.pointer = startNode.pointer
                startNode = nowNode
            else:
                nowNode.pointer = endNode.pointer
                endNode = nowNode


a = SinglyLinkedList()
a.insert(452)
a.insert(36)
a.insert(466)
print(a.recursive_count(a.head))
