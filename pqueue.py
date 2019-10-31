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



def test_priqueue(items, remove_item):
    #print(items)
    q = PriQueue()
    for item in items:
        q.push(item)
    
    # Remove the given item
    q.remove(remove_item)
    items.remove(remove_item)

    #for _ in range(len(items)):
    #    print(q.pop())
    
    # Verify that items come out in the proper order
    assert [ q.pop() for _ in range(len(items))] == sorted(items)
    #assert [ q.pop() for _ in range(len(items))] == (items)

if __name__ == '__main__':
    test_priqueue([4,3,7,10], 4)
    test_priqueue([9,2,1,8,5],2)
    test_priqueue([4,1,6],1)


