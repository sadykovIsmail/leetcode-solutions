import heapq


class MedianFinder:
    def __init__(self):
        # max_heap stores the smaller half of numbers (we push negative values to simulate it)
        self.max_heap = []

        # min_heap stores the larger half of numbers
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # Step 1: The Default Move
        # Always push into the max_heap (small half) first.
        heapq.heappush(self.max_heap, -num)

        # Step 2: Protect the Golden Rule
        # If the largest number in the small half is greater than the smallest number in the large half
        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        # Step 3: Fix the Balance
        # If max_heap becomes more than 1 element larger than min_heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        # If min_heap ever becomes larger than max_heap, we push one back
        # (This keeps the max_heap as the default holder for odd-length streams)
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self) -> float:
        # If the total number of elements is odd, max_heap will always have that 1 extra element
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])

        # If the total number of elements is even, we take the average of the two tops
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0
