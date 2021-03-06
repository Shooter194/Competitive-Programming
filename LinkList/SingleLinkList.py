#!/usr/bin/python
# -*- coding: utf-8 -*-

# Single LinkList implementation


class Node:

    # intialize function

    def __init__(self, val):
        self.value = val
        self.next = None


class LinkList:

    # initialize the linklist

    def __init__(self):
        self.head = None

    def printLinkList(self):
        temp = self.head
        while temp:
            print (temp.value)
            temp = temp.next
            
    def insertByNumber(self,num,newNode):
        temp = self.head
        if not temp:
            print ("Error: Linklist is empxty")
            return
            
        while temp and temp.value != num:
            temp = temp.next
            
        if not temp:
            print ("ERROR: Number not found")
        else:
            newNode.next = temp.next
            temp.next = newNode
            
    def insertByPostion(self,pos,newNode):
        temp = self.head
        count = 0
        
        while temp and count != pos:
            temp = temp.next
            
        if not temp:
            print ("Error: Linklist is shorter then the given position")
        else:
            newNode.next = temp.next
            temp.next = newNode
            
    def deleteByNumber(self,num):
        temp = self.head
        if not temp:
            print ("Linklist is Empty")
            return
        
        while temp.next and temp.next.value!=num:
            temp=temp.next
            
        if not temp.next:
            print ("Number not found")
        elif not temp.next.next:
            temp.next = None
        else:
            temp.next = temp.next.next


if __name__ == '__main__':

    linklist = LinkList()
    linklist.head = Node(3)
    linklist.head.next = Node(7)
    linklist.head.next.next = Node(9)
    linklist.head.next.next.next = Node(11)
    
    print("Before Modification in LinkList")
    linklist.printLinkList()
    
    # Checking insert function
    #l =  LinkList()   
    print ("After insert in LisnkList ")
    #l.insertByNumber(23,Node(23))
    linklist.insertByNumber(9,Node(23))
    linklist.printLinkList()
    
    # Linklist deletion 
    print ("After deletion in Linklist")
    linklist.deleteByNumber(9)
    linklist.printLinkList()