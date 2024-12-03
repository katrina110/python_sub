class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        else:
            data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return data

    def display_queue(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            current = self.front
            while current:
                print(current.data, end=" ")
                current = current.next
            print()

# Example usage:
queue = QueueLinkedList()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display_queue()  # Output: 1 2 3

queue.dequeue()
queue.display_queue()  # Output: 2 3

print("Is the queue empty?", queue.is_empty())  # Output: False
