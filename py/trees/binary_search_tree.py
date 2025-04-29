"""
Design your implementation of the binary tree.
A binary tree is the tree data structure in which each node has at most two children, refered two as left and right child
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Compare the new value with the parent node"""
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.value:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        elif data > node.value:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)
        else:
            return

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self._preorder_traversal(self.root, "")
        elif traversal_type == "inorder":
            return self._inorder_traversal(self.root, "")
        elif traversal_type == "postorder":
            return self._postorder_traversal(self.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False
    
    def _preorder_traversal(self, node, traversal):
        """Node->Left->Right"""
        if node:
            traversal += (str(node.value) + "-")
            traversal = self._preorder_traversal(node.left, traversal)
            traversal = self._preorder_traversal(node.right, traversal)
        return traversal

    def _inorder_traversal(self, node, traversal):
        """Left->Node->Right"""
        if node:
            traversal = self._inorder_traversal(node.left, traversal)
            traversal += (str(node.value) + "-")
            traversal = self._inorder_traversal(node.right, traversal)
        return traversal

    def _postorder_traversal(self, node, traversal):
        """Left->Right->Node"""
        if node:
            traversal = self._postorder_traversal(node.left, traversal)
            traversal = self._postorder_traversal(node.right, traversal)
            traversal += (str(node.value) + "-") 
        return traversal

    def __str__(self):
        return self.print_tree("inorder")


def main():
    print("               4")
    print("           /       \\")  
    print("          2          6")  
    print("         /  \\      /   \\")
    print("        1    3    5     7") 
    
    bst = BST()
    bst.insert(4)
    bst.insert(2)
    bst.insert(3)
    bst.insert(1)
    bst.insert(6)
    bst.insert(5)
    bst.insert(7)
    print("PreOrder Traversal: {}".format(bst.print_tree("preorder")))
    print("InOrder Traversal: {}".format(bst))
    print("PostOrder Traversal: {}".format(bst.print_tree("postorder")))


if __name__ == '__main__':
    main()
