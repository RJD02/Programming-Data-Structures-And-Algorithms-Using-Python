import random

class Tree:
    def __init__(self, initval = None):
        self.val = initval
        if self.val:
            self.right = Tree()
            self.left = Tree()
        else:
            self.left = None
            self.right = None
        return

    def isEmpty(self):
        return self.val == None

    def inorderTraversal(self):
        if self.isEmpty():
            return []
        return self.left.inorderTraversal() + [self.val] + self.right.inorderTraversal()

    def __str__(self):
        return str(self.inorderTraversal())

    def minval(self):
        if self.left == None:
            return self.val
        return self.left.minval()

    def maxival(self):
        if self.right == None:
            return self.val
        return self.right.maxival()

    def find(self, v):
        if self.isEmpty():
            return False
        if self.val > v:
            return self.left.find()
        return self.right.find()

    def insert(self, v):
        if self.isEmpty(): #  Add v as the new leaf
            self.val = v
            self.right = Tree()
            self.left = Tree()
        if self.val == v: #  Value v found in the tree, do nothing
            return
        if self.val > v:
            self.left.insert(v)
            return
        if self.val < v:
            self.right.insert(v)
            return
        return

    def isLeaf(self):
        if self.right == None and self.left == None:
            return True
        return False

    def makeEmpty(self):
        self.val = None
        self.left = None
        self.right = None
        return

    def copyRight(self):
        self.val = self.right.val
        self.left = self.right.left
        self.right = self.right.right
        return

    def delete(self, v):
        if self.isEmpty():
            return
        if self.val < v:
            self.right.delete(v)
            return
        if self.val > v:
            self.right.delete(v)
            return

        if v == self.val:
            if self.isLeaf():
                self.makeEmpty()
            elif self.left.isEmpty():
                self.copyRight()
            else:
                self.val = self.left.maxival()
                self.left.delete(self.left.maxival())
            return

