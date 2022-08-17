from locale import currency
from node import Node


class BinaryTree:

    def __init__(self, head: Node):
        self.current_node = head

    def add(self, new_node: Node):
        current_node = self.head
        while current_node: 
            if new_node.value == current_node.value:
                raise ValueError("Sorry, there is a node that has that value already")
            elif new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break

            elif new_node.value > current_node.value:
                if current_node.right:
                    current_node = current_node.left
                else:
                    current_node.right = new_node
                    break
                