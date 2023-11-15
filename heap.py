class HeapNode:
	def __init__(self, char, freq):
		self.char = char
		self.freq = freq
		self.left = None
		self.right = None

	# defining comparators less_than and equals
	def __lt__(self, other):
			return self.freq < other.freq

	def __eq__(self, other):
		if(other == None):
			return False
		if(not isinstance(other, HeapNode)):
			return False
		return self.freq == other.freq
    
class Heap:
    
    def __init__(self):
        self.heapList = []
        self.size = 0

    def parent(self, index : int) -> int:
        return (index -1) // 2
    
    def left_child(self, index : int) -> int:
        return 2 * index + 1
    
    def right_child(self, index : int) -> int:
        return 2 * index + 2
    
    def has_left(self, index : int) -> bool:
        return self.left_child(index) < self.size
    
    def has_right(self, index : int) -> bool:
        return self.right_child(index) < self.size
    
    def swap(self, i : int, j : int):
        self.heapList[i], self.heapList[j] = self.heapList[j], self.heapList[i]

    def up_heap(self, j : int):
        parent = self.parent(j)
        if j > 0:
            if self.heapList[j] < self.heapList[parent]:
                self.swap(j, parent)
                self.up_heap(parent)

    def down_heap(self, j : int):
        if self.has_left(j):
            left = self.left_child(j)
            small_child = left
            if self.has_right(j):
                right = self.right_child(j)
                if self.heapList[left] > self.heapList[right]:
                    small_child = right
            if self.heapList[small_child] < self.heapList[j]:
                self.swap(j, small_child)
                self.down_heap(small_child)
    
    def add(self, node : HeapNode):
        self.heapList.append(node)
        if (self.size > 0):
            self.up_heap(len(self.heapList)-1)
        self.size += 1

    def min(self) -> HeapNode:
        if self.size == 0:
            raise IndexError
        return self.heapList[0]
    
    def max(self) -> HeapNode:
        return max(self.heapList[len(self.heapList)//2:])
    
    def remove_min(self) -> HeapNode:
        if self.size == 0:
            raise IndexError
        self.swap(0, len(self.heapList)-1)
        node = self.heapList.pop()
        self.size -= 1
        self.down_heap(0)
        return node
    
    def remove_at(self, i : int) -> HeapNode:
        self.swap(i, len(self.heapList)-1)
        node = self.heapList.pop()
        self.size -= 1
        self.down_heap(i)
        return node
