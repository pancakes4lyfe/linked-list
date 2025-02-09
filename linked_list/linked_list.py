
# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node
        self.flag = False

# Defines the singly linked list
class LinkedList:
    def __init__(self, size = 0, tail = None, max = None):
        self.head = None # keep the head private. Not accessible outside this class
        self.size = size
        self.tail = tail

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        if self.head:
            return self.head.value
        return None


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        new_node = Node(value, next_node=self.head)
        if self.head == None:
            self.tail = new_node
        self.head = new_node
        self.size += 1

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(1)
    # Space Complexity: 0(1)
    def length(self):
        return self.size

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        value = None
        if (index + 1) <= self.length():
            current = self.head
            while index >= 0:
                value = current.value
                index -= 1
                current = current.next
        return value


    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        if self.tail:
            return self.tail.value
        return None

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_last(self, value):
        new_node = Node(value, next_node=None)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.add_first(value)
        

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        current = self.head
        if current:
            max_value = self.head.value
            while current:
                if current.value > max_value:
                    max_value = current.value
                current = current.next
            return max_value
        return None


    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        current = self.head
        if current:
            if current.value == value:
                self.head = current.next
                self.size -= 1
            else:
                while current:
                    if current.next and current.next.value == value:
                        current.next = current.next.next
                        self.size -= 1
                        if current.next == None:
                            self.tail = current
                    current = current.next


    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n^2) Yiikes!
    # Space Complexity: O(1)
    def reverse(self):
        current = self.head.next
        new_head = self.tail
        while current:
            if current.next == self.tail:
                self.tail.next = current
                self.tail = current
                if self.tail == self.head:
                    self.head = new_head
                    current = None
                else:
                    current = self.head
            else:
                current = current.next

    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        middle = self.size // 2
        return self.get_at_index(middle)

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        index = self.size - n - 1
        return self.get_at_index(index)

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(n)??
    # Space Complexity: O(1)

    # Hi Chris! I don't know why this doesn't pass the last test, and I kinda ran out of time to figure it out. Sorry!!
    def has_cycle(self):
        current = self.head
        while current:
            if current.flag:
                return True
            current.flag = True
            current = current.next
        return False

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head == None:
            return

        # navigate to last node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.head # make the last node link to first node
