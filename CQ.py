class Queue:
    def __init__(self): #starts the queue with the empty list
        self.items = []
    def enqueue(self, item): #Enqueuing the items into the list
        self.items.insert(0,item)
    def dequeue(self): #returns the popped item from the queue
        return self.items.pop() 
    def isEmpty(self): #returns True if the queue is empty
        return self.items == []
    def size(self): #returns size of the items in the queue in the list 
        return len(self.items)