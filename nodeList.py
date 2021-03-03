class Node:
    def __init__(self, initval = None):
        self.val = initval
        self.next = None

    def isEmpty(self):
        return self.val == None

    def append(self, v):
        if self.isEmpty():
            self.val = v
        elif self.next == None:
            new_node = Node(v)
            self.next = new_node
        else:
            (self.next).append(v)
        return

    def appendi(self, v):
        if self.isEmpty():
            self.val = v
            return
        temp = self
        while temp.next != None:
            temp = temp.next
        new_node = Node(v)
        temp.next = new_node
        return

    def print(self):
        new_node = self
        while(new_node != None):
            print(new_node.val, end = " ")
            new_node = new_node.next
        print()
        return

    def insert(self, v):
        if self.isEmpty():
            self.val = v
            return
        new_node = Node(v)
        self.val, new_node.val = new_node.val, self.val
        self.next, new_node.next = new_node, self.next
        #  new_node.next = self.next
        #  self.next = new_node.next
        return

    def delete(self, v):
        if self.isEmpty():
            return
        if self.val == v:
            self.val = self.next.val
            self.next = self.next.next
            return
        if self.next.val == v:
            self.next = self.next.next
            return
        self.next.delete(v)
        return

    def delete(self, v):
        if self.isEmpty():
            return
        if self.val == v:
            if self.next == None:
                self.val = None
            else:
                self.val = self.next.val
                self.next = self.next.next
                return
        temp =  self
        while temp.next != None:
            if temp.next.val == v:
                temp.next = temp.next.next
                return
            else:
                temp = temp.next
        return

    def deleter(self, v):
        if self.isEmpty():
            return
        if self.val == v:
            if self.next == None:
                self.val = None
            else:
                self.val = self.next.val
                self.next = self.next.next
                return
        else:
            if self.next != None:
                self.next.deleter(v)
                if self.next.val == None:
                    self.next = self.next.next
        return

    def __str__(self):
        selflist = []
        if self.val == None:
            return str(selflist)
        temp = self
        selflist.append(temp.val)
        while temp.next != None:
            temp = temp.next
            selflist.append(temp.val)
        return str(selflist)
