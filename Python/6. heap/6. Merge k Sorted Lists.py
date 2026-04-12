# Definition for singly-linked list.
"""
23. Merge k Sorted Lists
Hard
Topics
premium lock icon
Companies
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import List, Optional
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        # if not lists or not lists[0]:
        #     return ListNode(None)
        for linkedList in lists:
            if not linkedList:
                continue
            head = linkedList
            while head:
                heapq.heappush(minHeap, head.val)
                head = head.next
        if minHeap:
            newHead = ListNode(heapq.heappop(minHeap))
            point = newHead
        
            while minHeap:
                point.next = ListNode(heapq.heappop(minHeap))
                point = point.next
            return newHead
        else:
            return None

# head = ListNode(1)
# node2 = ListNode(4)
# node3 = ListNode(5)
# head.next = node2
# node2.next = node3

# head2 = ListNode(1)
# node22 = ListNode(3)
# node23 = ListNode(4)
# head2.next = node22
# node22.next = node23

# head3 = ListNode(2)
# node32 = ListNode(6)
# head3.next = node32

# lists = []
# lists.append(head)
# lists.append(head2)
# lists.append(head3)

example = Solution()
print(example.mergeKLists([]))

