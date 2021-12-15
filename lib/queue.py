import heapq


# Priority queue
class PriorityQueue:

    def __init__(self):
        self._hq = []
        self._mp = {}  # Keep all items in a map so lookup becomes faster

    def push(self, priority, item):
        heapq.heappush(self._hq, (priority, item))
        self._mp[item] = item

    def pop(self):
        the_tuple = heapq.heappop(self._hq)
        item = the_tuple[1]
        del self._mp[item]
        return item

    def get(self, item):
        return self._mp.get(item, None)

    def update_priority(self, new_priority, item):
        for i in range(len(self._hq)):
            it = self._hq[i]
            if item == it[1]:
                self._hq[i] = (new_priority, item)
                heapq.heapify(self._hq)
                return

    def __len__(self):
        return len(self._hq)

    def __iter__(self):
        return self

    def __next__(self):
        if self._hq:
            return self.pop()
        else:
            raise StopIteration()
