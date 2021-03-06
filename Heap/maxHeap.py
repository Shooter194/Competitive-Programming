


import sys

class MaxHeap:

    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.size = 1
        self.Heap = [0]*(maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.Front = 1
        
        
    def parent(self,pos):
        return pos // 2
        
    def leftChild(self,pos):
        return 2*pos
        
    def rightChild(self,pos):
        return (2*pos + 1) 
        
    def swap(self,fpos,spos):
        self.Heap[fpos],self.Heap[spos] =  (self.Heap[spos],self.Heap[fpos])
        
    def isLeaf(self, pos):
        if (pos > self.size//2 and pos <= self.size):
            return True
        return False
        
    def maxHeapify(self,pos):
        if not self.isLeaf(pos):
            if ( self.Heap[pos] < self.Heap[self.leftChild(pos)] or self.Heap[pos] < self.Heap[self.rightChild(pos)] ):
                if ( self.Heap[self.leftChild(pos)] >= self.Heap[self.rightChild(pos)] ):
                    self.swap(pos,self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))
                else:
                    self.swap(pos,self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))
                    
    def insert(self,element):
        if self.size >= self.maxsize:
            return
            
        self.size += 1
        self.Heap[self.size] = element
        
        current = self.size
        
        while(self.Heap[current] > self.Heap[self.parent(current)]):
            self.swap(current,self.parent(current))
            current = self.parent(current)
            
    def printHeap(self):
        
        print (self.Heap[1:])
        
    def extractMax(self):
        popped = self.Heap[self.Front]
        self.Heap[self.Front] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.Front)
        
        return popped
        
        
if __name__ == "__main__":

    maxheap = MaxHeap(15)
    maxheap.insert(5)
    maxheap.insert(3)
    maxheap.insert(17)
    maxheap.insert(10)
    maxheap.insert(84)
    maxheap.insert(19)
    maxheap.insert(6)
    maxheap.insert(22)
    maxheap.insert(9)
    
    maxheap.printHeap()
    
    print ("Max Value: {}".format(str(maxheap.extractMax())))
    print ("Max Value: {}".format(str(maxheap.extractMax())))
    