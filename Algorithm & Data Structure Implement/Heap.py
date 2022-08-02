class Heap:
    def __init__(self):
        self.heap = []

    def heappush(self, data):
        i = len(self.heap)
        self.heap.append(data)

        while i > 0:
            parent = (i - 1) // 2

            if self.heap[parent] <= self.heap[i]:
                break

            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent

    def heappop(self):
        if not self.heap:
            raise Exception("pop from empty heap")

        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        i = 0
        last = len(self.heap) - 1

        while i < last:
            child = 2 * i + 1
            if child < last and self.heap[child] > self.heap[child + 1]:
                child += 1

            if child > last or self.heap[i] <= self.heap[child]:
                break

            self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
            i = child

        return root


heap = Heap()
for num in [4, 3, 5, 1, 2, 6, 7]:
    heap.heappush(num)

while True:
    print(heap.heappop())
