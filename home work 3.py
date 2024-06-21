class MinHeap:
def init(self):
    self.heap = []

def parent(self, i):
    return (i - 1) // 2

def left_child(self, i):
    return 2 * i + 1

def right_child(self, i):
    return 2 * i + 2

def insert_key(self, key):
    self.heap.append(key)
    i = len(self.heap) - 1
    while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
        self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
        i = self.parent(i)

def heapify(self, i):
    smallest = i
    left = self.left_child(i)
    right = self.right_child(i)

    if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
        smallest = left

    if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
        smallest = right

    if smallest != i:
        self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
        self.heapify(smallest)

def extract_min(self):
    if len(self.heap) == 0:
        return None
    if len(self.heap) == 1:
        return self.heap.pop()

    root = self.heap[0]
    self.heap[0] = self.heap.pop()
    self.heapify(0)

    return root

def heap_sort(arr):
    heap = MinHeap()
    sorted_arr = []
    for num in arr:
        heap.insert_key(num)

    for _ in range(len(arr)):
        sorted_arr.append(heap.extract_min())

    return sorted_arr
input_numbers = [1,8,5,10,2,23,20,51]
sorted_numbers = heap_sort(input_numbers)
print(sorted_numbers)