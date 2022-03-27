from enum import Enum
from typing import Any, Callable
from typing import Optional
from typing import Dict, List


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


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, data1, data2, weight: Optional[float] = None):
        self.source = Vertex(data1)
        self.destination = Vertex(data2)

    def pokaz(self):
        print(self.source.data, "-->", self.destination.data)


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies = {}

    def create_vertex(self, data: Any) -> Vertex:
        self.adjacencies[Vertex(data)] = []
        return Vertex(data)

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.adjacencies.get(source, Edge(source, destination, weight))

    def add_undirected_edge(self, source: Vertex, destination: Vertex) -> None:
        self.adjacencies.get(source, (Edge(source, destination)))
        self.adjacencies.get(destination, (Edge(destination, source)))

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge == 1:
            self.adjacencies.get(source, Edge(source, destination, weight))
        if edge == 2:
            self.adjacencies.get(destination, Edge(destination, source, weight))

    def dft(self, v: Vertex, visited: List[Vertex], visit: Callable[[Any], None]) -> None:
        visit(v)
        visited.append(v)
        self.adjacencies.get(v)
        if self.adjacencies.get(v) is not None:
            for neighbour in self.adjacencies.get(v):
                if neighbour.destination not in visited:
                    visited.append(neighbour.destination)
                    self.dft(neighbour.destination, visited, visit)


graph = Graph()
graph.create_vertex('v1')
graph.create_vertex('v2')
graph.create_vertex('v3')
graph.create_vertex('v4')
graph.create_vertex('v5')
graph.add(2, 'v0', 'v1')
graph.add(2, 'v0', 'v5')
graph.add(2, 'v5', 'v4')
graph.add(2, 'v4', 'v3')
graph.add(2, 'v3', 'v2')
graph.add(2, 'v2', 'v1')
graph.dft('v0', list(), print)











