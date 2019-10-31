import heapq

class PriQueue:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)

    def remove(self, item):
        self.heap.remove(item)



def test_priqueue():
    q = PriQueue()
    q.push(4)
    q.push(3)
    q.push(7)
    q.push(10)
    q.remove(4)
    assert [ q.pop() for _ in range(3) ] == [3, 7, 10]

if __name__ == '__main__':
    test_priqueue()

