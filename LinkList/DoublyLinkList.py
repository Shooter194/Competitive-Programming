 # Doubly LinkList Implementation

import random

class DoublyLinklist():
    def __init__(self):
        self.front = None
        self.end = None
        
    def insertAtLast(self,doublyNode):
        temp = self.end
        
        if not temp:
            self.front = doublyNode
            self.end = doublyNode
            return
        
        doublyNode.leftNext = temp
        temp.rightNext = doublyNode
        self.end = doublyNode
        
    def insertAtBeg(self,doublyNode):
        temp = self.front
        
        if not temp:
            self.front = doublyNode
            self.end = doublyNode
            return
        
        temp.leftNext = doublyNode
        doublyNode.rightNext = temp
        self.front = doublyNode
        
    def printDoublyll(self):
        temp = self.front
        
        while temp:
            print (temp.value)
            temp = temp.rightNext


    def deleteByNumber(self,num):
        temp = self.front
         
        if not temp:
            print("Empty Linklist")
            return

        while temp:
            if temp.value == num:
                if not (temp.rightNext or temp.leftNext):
                    self.front = None
                    self.end  = None
                elif not (temp.rightNext):
                    self.end = temp.leftNext
                    self.end.rightNext = None
                    temp.leftNext = None
                elif not (temp.leftNext):
                    self.front = temp.rightNext
                    self.front.leftNext = None
                    temp.rightNext = None
                else:
                    temp.leftNxt.rightNext = temp.rightNext
                    temp.rightNext.leftnext = temp.leftNext
                    temp.rightNext = None
                    temp.leftNext = None
                     
            temp = temp.rightNext
                     
                     
        

class DoublyNode():
    def __init__(self,val):
        self.value = val
        self.rightNext = None
        self.leftNext = None
        
if __name__ == "__main__":

    doublylinklist = DoublyLinklist()
    for i in range(6):
        #doublylinklist.insert(DoublyNode(random.randrange(1,100,7)))
        doublylinklist.insertAtLast(DoublyNode(i))
        doublylinklist.insertAtBeg(DoublyNode(i))
        
    doublylinklist.printDoublyll()
    doublylinklist.deleteByNumber(5)
    doublylinklist.printDoublyll()
