import heapq


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, node):
        heuristic_conjecture = node.f
        heapq.heappush(self.heap, (heuristic_conjecture, node))

    def pop(self):
        return heapq.heappop(self.heap)[1]
