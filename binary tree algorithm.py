
"""
        1
       / \
      2   3
     / \  /\
    4   5 6 7
output 1. 4 2 5 1 6 3 7 
output 2. 1 2 4 5 3 6 7 
output 3. 4 5 2 6 7 3 1 
"""





class BST:
    def __init__(self,key = None):
        self.key = key
        self.lchild = None
        self.rchild = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def inorder(self):
        if (self.root == None):
             print("tree is empty")
        else:
            self._inorder(self.root)
    def _inorder(self,current):
        if current:
            """change print function according to your required output 
                 place print function at top for output 1
                 place print function at in middle for output 2
                 place print function at bottom for output 3"""
            self._inorder(current.lchild)
            self._inorder(current.rchild)
            print(current.key ,end=" ")




obj = BinaryTree()
first = BST(1)
second = BST(2)
third = BST(3)
fourth = BST(4)
fifth = BST(5)
sixth = BST(6)
seventh = BST(7)
obj.root = first
first.lchild = second
first.rchild = third
second.lchild = fourth
second.rchild = fifth
third.lchild = sixth
third.rchild = seventh
obj.inorder()
