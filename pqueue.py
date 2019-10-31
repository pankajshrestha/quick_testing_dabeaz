import heapq
from hypothesis import given
from hypothesis.strategies import lists, integers

class PriQueue:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)

    def remove(self, item):
        self.heap.remove(item)
        heapq.heapify(self.heap) ## Did not undestand why there is a bug, visually the list are matching, not sure how this line addresses the bug


@given(lists(integers(min_value=0, max_value=9),
            unique=True, min_size=10, max_size=10),
            integers(min_value=0, max_value=9))
def test_priqueue(items, remove_item):
    #print(items)
    print('Trying with:', items, remove_item)
    q = PriQueue()
    for item in items:
        q.push(item)
    
    # Remove the given item
    q.remove(remove_item)
    items.remove(remove_item)

    #for _ in range(len(items)):
    #    print(q.pop())
    
    pop_list = [q.pop() for _ in range(len(items))]
    # Verify that items come out in the proper order
    print('Assert Visual Test:', pop_list, sorted(items))
    #assert [ q.pop() for _ in range(len(items)) ] == sorted(items)
    assert pop_list == sorted(items)
    

if __name__ == '__main__':
    test_priqueue()
    


