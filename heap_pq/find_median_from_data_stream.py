"""
Problem No. 295

The median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value, and the median is the mean of the two middle values.

- For example, for arr = [2,3,4], the median is 3.
- For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:
- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data structure.
- double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual 
answer will be accepted.

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
"""

class MedianFinder:

    def __init__(self):
        # small is a maxheap, large is a minheap
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # by default, add to small
        heapq.heappush(self.small, num * -1)

        # make sure every element in small <= in large
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # if size diff > 1
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        else:
            return ((-1 * self.small[0]) + self.large[0]) / 2


    """
    def __init__(self):
        self.list = []

    def addNum(self, num: int) -> None:
        self.list.append(num)

    def findMedian(self) -> float:
        lst = self.heap_to_lst()

        mid = (len(lst) // 2)
        print(lst)
        if len(lst) % 2 != 0:
            return lst[mid]
        else:
            return (lst[mid] + lst[mid-1]) / 2

    def heap_to_lst(self):
        ans = []
        copy = self.list.copy()
        heapq.heapify(copy)

        while copy:
            ans.append(heappop(copy))

        return ans
    """

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()