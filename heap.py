class Item:

    def __init__(self, k, v):
        self.key = k
        self.value = v

    def is_empty(self):
        return len(self) == 0

    def __lt__(self, other):
        return self.key < other.key
    
    def __gt__(self, other):
        return self.key > other.key
    
class Heap:
    
    def __init__(self):
        self.heapList = []
        self.size = 0

    def parent(self, index):
        return (index -1) // 2
    
    def left_child(self, index):
        return 2 * index + 1
    
    def right_child(self, index):
        return 2 * index + 2
    
    def has_left(self, index):
        return self.left_child(index) < self.size
    
    def has_right(self, index):
        return self.right_child(index) < self.size
    
    def swap(self, i, j):
        self.heapList[i], self.heapList[j] = self.heapList[j], self.heapList[i]

    def up_heap(self, j):
        parent = self.parent(j)
        if j > 0: # chegou no nós raiz
            if self.heapList[j] < self.heapList[parent]: # compara o nó filho com seu pai, se o filho for menor que o pai, swap
                self.swap(j, parent)
                self.up_heap(parent)

    def down_heap(self, j):
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

    def add(self, key, value):
        self.heapList.append(Item(key, value))
        if (self.size > 0):
            self.up_heap(len(self.heapList)-1)
        self.size += 1

    def min(self):
        if self.size == 0:
            raise IndexError
        item = self.heapList[0]
        return (item.key, item.value)
    
    def max(self):
        folhas = self.heapList[len(self.heapList)//2:]
        maior = max(folhas)
        return (maior.key, maior.value)
    
    def remove_min(self):
        if self.size == 0:
            raise IndexError
        self.swap(0, len(self.heapList)-1)
        item = self.heapList.pop()
        self.size -= 1
        self.down_heap(0)
        return (item.key, item.value)
    
    def remove_at(self, i):
        self.swap(i, len(self.heapList)-1)
        item = self.heapList.pop()
        self.size -= 1
        self.down_heap(i)
        return (item.key, item.value)
