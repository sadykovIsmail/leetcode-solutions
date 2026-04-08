"""
Left Child: 2i + 1
Right Child: 2i + 2
Parent: (i - 1) // 2

template:
"""
class MinHeapFromScrach:

    def __init__(self):
        self.heap = []
        
    def peek(self):
        # The smallest item is ALWAYS at the very top (index 0)
        if len(self.heap) > 0:
            return self.heap[0]
        return None
    
    def push(self, val):
        # 1. Add the new value to the very end of the array
        self.heap.append(val)
        
        # 2. Get its starting index
        current_idx = len(self.heap) - 1
        
        # 3. Bubble Up!
        # While we aren't at the root, AND we are smaller than our parent
        while current_idx > 0:
            parent_idx = (current_idx - 1) // 2
            
            if self.heap[current_idx] < self.heap[parent_idx]:
                # Swap them!
                self.heap[current_idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[current_idx]
                # Move our pointer up to the parent's old spot
                current_idx = parent_idx
            else:
                # If we are bigger than our parent, we found our perfect spot. Stop.
                break

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop() # Only one item, just pop it normally
            
        # 1. Save the smallest value to return later
        min_val = self.heap[0]
        
        # 2. Move the very last item in the array to the top (index 0)
        self.heap[0] = self.heap.pop()
        
        # 3. Bubble Down!
        current_idx = 0
        
        while True:
            left_child_idx = 2 * current_idx + 1
            right_child_idx = 2 * current_idx + 2
            smallest_idx = current_idx # Assume current is the smallest for now
            
            # Check if left child exists AND is smaller than current
            if left_child_idx < len(self.heap) and self.heap[left_child_idx] < self.heap[smallest_idx]:
                smallest_idx = left_child_idx
                
            # Check if right child exists AND is smaller than whoever is currently 'smallest'
            if right_child_idx < len(self.heap) and self.heap[right_child_idx] < self.heap[smallest_idx]:
                smallest_idx = right_child_idx
                
            # If the smallest is still our current index, we are in the right spot! Stop.
            if smallest_idx == current_idx:
                break
                
            # Otherwise, swap with the smallest child and keep moving down
            self.heap[current_idx], self.heap[smallest_idx] = self.heap[smallest_idx], self.heap[current_idx]
            current_idx = smallest_idx
            
        return min_val
    

# Min heap using with heapq

import heapq

# Start with a messy list
nums = [5, 7, 9, 1, 3]

# 1. HEAPIFY: Rearrange the list into a valid Min-Heap (O(N) time)
heapq.heapify(nums)

# 2. PEEK: Look at the smallest number without removing it (O(1) time)
# (It is always sitting at index 0)
smallest = nums[0]

# 3. POP: Remove and return the smallest number (O(log N) time)
# (The heap automatically fixes itself after)
smallest = heapq.heappop(nums)

# 4. PUSH: Add a brand new number (O(log N) time)
# (The heap automatically bubbles it to the right spot)
heapq.heappush(nums, 2)