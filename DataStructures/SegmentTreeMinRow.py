class Node():
    def __init__(self, left, right, value):
        self.leftNode = None
        self.rightNode = None
        self.left = left
        self.right = right
        self.max = value
        self.sum = value
        
class SegmentTree:
    def __init__(self, size, value):
        self.value = value
        self.root = self._build(0, size - 1, value)
        self.start = 0
        
    def _build(self, left, right, value):
        if left == right:
            return Node(left, right, value)
        mid = (left + right)//2
        node = Node(left, right, value)
        node.leftNode = self._build(left, mid, value)
        node.rightNode = self._build(mid + 1, right, value)
        node.max = value
        node.sum = node.leftNode.sum + node.rightNode.sum
        return node
    
    def upgrade(self, value, index):
        self._upgrade(self.root, value, index)
        
    def _upgrade(self, node, value, index):
        if node.left == node.right:
            node.max += value
            node.sum += value
            return
        mid = (node.left + node.right)//2
        if index <= mid:
            self._upgrade(node.leftNode, value, index)
        else:
            self._upgrade(node.rightNode, value, index)
        node.max = max(node.leftNode.max, node.rightNode.max)
        node.sum = node.leftNode.sum + node.rightNode.sum
    
    def findMinIndex(self, value, maxRow):
        if self.root.max < value:
            return -1
        return self._findMinIndex(self.root, value, maxRow)
    
    def _findMinIndex(self, node, value, maxRow):
        if not node.leftNode and not node.rightNode:
            return node.left
        if node.leftNode and node.leftNode.max >= value:
            return self._findMinIndex(node.leftNode, value, maxRow)
        if node.rightNode and node.rightNode.left <= maxRow and node.rightNode.max >= value:
            return self._findMinIndex(node.rightNode, value, maxRow)
        return -1
        
    def query(self, index):
        return self._query(self.root, index)
        
    def _query(self, node, index):
        if node.left == node.right:
            return node.max
        mid = (node.left + node.right)//2
        if index <= mid:
            return self._query(node.leftNode, index)
        else:
            return self._query(node.rightNode, index)
            
    def querySum(self, maxRow):
        return self._querySum(self.root, maxRow)
        
    def _querySum(self, node, maxRow):
        if node.left == node.right:
            return node.sum
        mid = (node.left + node.right)//2
        if maxRow > mid:
            return node.leftNode.sum + self._querySum(node.rightNode, maxRow)
        return self._querySum(node.leftNode, maxRow)
        
