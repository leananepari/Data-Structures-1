import sys
# sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
      new_node = BinarySearchTree(value)

      def helper(node, new_node):
        if new_node.value >= node.value:
          if node.right == None:
            node.right = new_node
          else:
            helper(node.right, new_node)
        elif new_node.value <= node.value:
          if node.left == None:
            node.left = new_node
          else:
            helper(node.left, new_node)

      if value <= self.value:
        if self.left == None:
          self.left = new_node
        else:
          helper(self.left, new_node)

      elif value >= self.value:
        if self.right == None:
          self.right = new_node
        else:
          helper(self.right, new_node)

        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

      def helper(node, target):
        if node.value == target:
          return True
        else:
          if target >= node.value:
            if node.right == None:
              return False
            else:
              helper(node.right, target)
          elif target <= node.value:
            if node.left == None:
              return False
            else:
              helper(node.left, target)
      
      if target == self.value:
        return True
      elif target >= self.value:
        return helper(self.right, target)
      elif target <= self.value:
        return helper(self.left, target)

    # Return the maximum value found in the tree
    def get_max(self):
      max = self.value

      def helper(node):
        nonlocal max
        if node.value > max:
          max = node.value
        if node.right == None:
          return
       
        helper(node.right)
      
      if self.right == None:
        return max
      else:
        helper(self.right)
      return max

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

bst = BinarySearchTree(5)
bst.insert(2)
bst.insert(3)
bst.insert(7)
bst.insert(6)
print(bst.right.left.value)
print(bst.contains(6))