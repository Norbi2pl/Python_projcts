from typing import Any


class Node:
    value: Any
    next: 'Node'

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    head: Node
    tail: Node

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def push(self, value: Any) -> None:
        node_list: Node = Node(value)
        node_list.next = self.head
        self.head = node_list

    def append(self, value: Any) -> None:
        last_node: Node = Node(value)
        list_head: Node = self.head
        while list_head.next is not None:
            list_head = list_head.next

        list_head.next = last_node

    def node(self, at: int) -> Node:
        list_head: Node = self.head
        for i in range(0, at + 1):
            if i == at:
                return list_head.value
            list_head = list_head.next

    def insert(self, value: Any, after: Node) -> None:
        list_head: Node = self.head
        while list_head.value != after:
            list_head = list_head.next
        node_list: Node = Node(value)
        node_list.next = list_head.next
        list_head.next = node_list

    def pop(self) -> Any:
        list_head_tmp: Node = self.head
        self.head = self.head.next
        return list_head_tmp.value

    def remove_last(self) -> Any:
        list_head: Node = self.head
        while list_head.next.next is not None:
            list_head = list_head.next
        list_head_tmp: Node = list_head.next
        list_head.next = None
        return list_head_tmp.value

    def remove(self, after: Node) -> Any:
        list_head: Node = self.head
        while list_head.value != after:
            list_head = list_head.next
        list_head_tmp = list_head.next
        list_head.next = list_head.next.next
        return list_head_tmp.value

    def __str__(self) -> str:
        wynik: str = ''
        list_next: Node = self.head
        while list_next.next is not None:
            wynik += str(list_next.value) + '->'
            list_next = list_next.next
        wynik += str(list_next.value)
        return wynik

    def __len__(self) -> int:
        list_head: Node = self.head
        length: int = 0
        while list_head.next is not None:
            length += 1
            list_head = list_head.next
        length += 1
        return length


# list_ = LinkedList()
# list_.push(1)
# list_.push(2)
# list_.push(3)
# list_.append(9)
# # print(list_.node(2))
# list_.insert(5, 1)
# print(list_.pop())
# list_.remove_last()
# list_.remove(2)
# print(list_)
# print(list_.__len__())


class Stack:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def push(self, element: Any) -> None:
        self._storage.push(element)

    def pop(self):
        stack_head: Node = self._storage.head
        while stack_head.next.next is not None:
            stack_head = stack_head.next
        stack_head_tmp: Node = stack_head.next
        stack_head.next = None
        return stack_head_tmp.value

    def __str__(self) -> str:
        wynik: str = ''
        stack_next: Node = self._storage.head
        while stack_next.next is not None:
            wynik += str(stack_next.value) + '\n'
            stack_next = stack_next.next
        wynik += str(stack_next.value)
        return wynik

    def __len__(self) -> int:
        stack_ele: Node = self._storage.head
        length: int = 0
        while stack_ele.next is not None:
            length += 1
            stack_ele = stack_ele.next
        length += 1
        return length


# stack = Stack()
# stack.push(12)
# stack.push(13)
# stack.push(14)
# stack.push(15)
# stack.pop()
# stack.push(16)
# stack.push(17)
# print(stack)
# print(stack.__len__())


class Queue:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def peek(self) -> Any:
        queue_ele: Node = self._storage.head
        while queue_ele.next is not None:
            queue_ele = queue_ele.next
        return queue_ele.value

    def enqueue(self, element: Any) -> None:
        self._storage.push(element)

    def dequeue(self) -> Any:
        queue_head: Node = self._storage.head
        while queue_head.next.next is not None:
            queue_head = queue_head.next
        queue_head_tmp: Node = queue_head.next
        queue_head.next = None
        return queue_head_tmp.value

    def __str__(self) -> str:
        wynik: str = ''
        queue_next: Node = self._storage.head
        while queue_next.next is not None:
            wynik += str(queue_next.value) + ' , '
            queue_next = queue_next.next
        wynik += str(queue_next.value)
        return wynik

    def __len__(self) -> int:
        queue_ele: Node = self._storage.head
        length: int = 0
        while queue_ele.next is not None:
            length += 1
            queue_ele = queue_ele.next
        length += 1
        return length


# queue = Queue()
# queue.enqueue(10)
# queue.enqueue(15)
# queue.enqueue(20)
# queue.enqueue(25)
# print(queue.dequeue())
# print(queue.peek())
# print(queue)
# print(queue.__len__())
