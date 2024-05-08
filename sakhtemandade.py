class Queue:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size
        def is_empty(self):
            return len(self.items) == 0
            def is_full(self):
                return len(self.items) == self.max_size
                def enqueue(self, item):
                    if not self.is_full():
                        self.items.append(item)
                        else:
                             print("Queue is full")
                             def dequeue(self):
                                  if not self.is_empty():
                                       return self.items.pop(0)
                                        else:
                                            return None
                                            def front(self):
                                                if not self.is_empty():
                                                    return self.items[0]
                                                    else:
                                                        return None
                                                        def size(self):
                                                            return len(self.items)
                                                            def get_element_at_index(self, index):
                                                                if 0 <= index < len(self.size):
                                                                    return self.items[index]
                                                                    else:
                                                                        return None
                                                                        def get_element_at_index(self, index):
                                                                            if 0 <= index < len(self.size):
                                                                                return self.items[index]
                                                                                else:
                                                                                    return None
                                                                                    q.enqueue("ra'na")
                                                                                    q.enqueue("vez")
                                                                                    q.enqueue("Arya")
                                                                                    print("queue size is:", q.size())
                                                                                    print(q.dequeue(), "left the queue")
                                                                                    print("front of queue is:", q.front())
                                                                                    q.enqueue("milda")
                                                                                    q.dequeue()
                                                                                    q.dequeue()
                                                                                    q.dequeue()
                                                                                    print("It was a queue")