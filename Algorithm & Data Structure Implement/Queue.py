class CircularQueue:
    def __init__(self, max_size):
        self.head = 0
        self.rear = 0
        self.max_size = max_size
        self.queue = [0 for _ in range(max_size)]

    @property
    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    @property
    def is_empty(self):
        return self.rear == self.head

    def push(self, data):
        if self.is_full():
            raise Exception("Queue is full")
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = data

    def pop(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        self.front = (self.front + 1) % self.max_size
        return self.queue[self.front]


class Queue:
    class _Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.rear = None
        self.size = 0

    @property
    def is_empty(self):
        if self.size > 0:
            return False
        return True

    @property
    def front(self):
        if self.size > 0:
            return self.head.data
        return -1

    @property
    def back(self):
        if self.size > 0:
            return self.rear.data
        return -1

    def enqueue(self, data):
        node = self._Node(data)
        if self.is_empty:
            self.head = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size += 1

    def dequeue(self):
        if self.is_empty:
            raise Exception("Queue is empty")

        self.size -= 1
        temp = self.head.data
        self.head = self.head.next
        return temp


queue = Queue()

numbers = [4, 2, 3, 6, -1, 3, 5]
for number in numbers:
    queue.enqueue(number)

print(f"front: {queue.front}")
print(f"back: {queue.back}")


while not queue.is_empty:
    print(queue.dequeue())

queue.dequeue()
