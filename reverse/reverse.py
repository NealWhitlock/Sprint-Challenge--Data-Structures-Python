class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    # def reverse_list(self, node, prev):
        
        """ Recursive Approach """
        # def recursive_reverse(current, previous):
        # # Helper function to keep track of the recursion
        #     if not current:  # If no node because we're at the end
        #         return previous  # return the previous one
            
        #     new = current.next_node  # saved pointer to next node
        #     current.next_node = previous  # reverse order
        #     previous = current  # current node set to previous for next recursion
        #     current = new  # current becomes the next
        #     return recursive_reverse(current, previous)  # Recurse on the function
        
        # # Update the head as the recursion moves along
        # self.head = recursive_reverse(current=self.head, previous=None)


        """ Iterative Approach """
        # if not self.head:  # If it doesn't exist then be done
        #     return None
        # else:
        #     current = self.head  # start with the head
        #     new = current.next_node  # the next node is set as new
        #     current.next_node = None  # the current one (head) points to None
        #     while new is not None:  # loop through nodes until we get to the tail
        #         previous = current  # the head gets stored as previous
        #         current = new  # the second node is set to current
        #         new = current.next_node  # third node gets stored as new
        #         current.next_node = previous  # the head gets pointed to by the current node
        #     self.head = current  # what was the tail becomes the head


    """ Straight-Forward Recursive Approach (Solution) """
    def reverse_list(self, node,  prev):
        # Nothing changes in empty or single lists
        if node is None:
            return
        if node.next_node is None:
            self.head = node
            self.head.next_node = prev
        else:
            self.reverse_list(node.next_node, node)
            node.next_node = prev
