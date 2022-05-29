class BSTNode:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class BST:
    def __init__(self):
        self.root = None
    def getRoot(self):
        return self.root
    def add(self, val):
        if self.root is None:
            self.root = BSTNode(val)
        else:
            self._add(val, self.root)
    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = BSTNode(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = BSTNode(val)
    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None
    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.l is not None):
            return self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            return self._find(val, node.r)
    def deleteTree(self):
        self.root = None
    def delete(self, key):
        self.root = self._delete(key, self.root)
    def _delete(self, key, root):
        if not root: 
            return None
        if root.v == key:
            if not root.r: return root.l
            if not root.l: return root.r
            if root.l and root.r:
                temp = root.r
                while temp.l: temp = temp.l
                root.v = temp.v
                root.r = self._delete(root.v, root.r)
        elif root.v > key:
            root.l = self._delete(key, root.l)
        else:
            root.r = self._delete(key, root.r)
        return root
    def print(self):
        if self.root is not None:
            self._printTree(self.root)
        print()
    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ', end = ' ')
            self._printTree(node.r)
    def min(self):
        current = self.root
        while(current.l is not None):
            current = current.l
        return current.v
    def max(self):
        current = self.root
        while(current.r is not None):
            current = current.r
        return current.v
