#!/usr/bin/python3
# Define a class named Node
class Node:
    # Define a private instance attribute named data
    __data = 0
    # Define a private instance attribute named next_node
    __next_node = None

    # Define a constructor method that takes two arguments, data and next_node
    def __init__(self, data, next_node=None):
        # Assign the arguments to the private attributes using the setters
        self.data = data
        self.next_node = next_node

    # Define a property getter for the data attribute
    @property
    def data(self):
        # Return the value of the private attribute data
        return self.__data

    # Define a property setter for the data attribute
    @data.setter
    def data(self, value):
        # Check if the value is an integer, otherwise raise a TypeError exception
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        # Assign the value to the private attribute data
        self.__data = value

    # Define a property getter for the next_node attribute
    @property
    def next_node(self):
        # Return the value of the private attribute next_node
        return self.__next_node

    # Define a property setter for the next_node attribute
    @next_node.setter
    def next_node(self, value):
        # Check if the value is None or a Node instance, otherwise raise a TypeError exception
        if not (value is None or isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        # Assign the value to the private attribute next_node
        self.__next_node = value

# Define a class named SinglyLinkedList
class SinglyLinkedList:
    # Define a private instance attribute named head
    __head = None

    # Define a constructor method that takes no arguments
    def __init__(self):
        # Initialize the head attribute to None
        self.__head = None

    # Define a public instance method named sorted_insert that takes one argument, value
    def sorted_insert(self, value):
        # Create a new Node instance with the given value
        new_node = Node(value)
        # Check if the list is empty or the value is smaller than the head's data
        if self.__head is None or value < self.__head.data:
            # Insert the new node at the beginning of the list
            new_node.next_node = self.__head
            self.__head = new_node
        # Otherwise, traverse the list to find the correct position for the new node
        else:
            # Initialize a current node and a previous node
            current = self.__head
            previous = None
            # Loop until the end of the list or the value is smaller than the current node's data
            while current and value >= current.data:
                # Update the previous node and the current node
                previous = current
                current = current.next_node
            # Insert the new node between the previous node and the current node
            new_node.next_node = current
            previous.next_node = new_node

    # Define a special method named __str__ that takes no arguments
    def __str__(self):
        # Initialize an empty string to store the list representation
        list_str = ""
        # Initialize a current node
        current = self.__head
        # Loop until the end of the list
        while current:
            # Add the current node's data to the string, followed by a new line
            list_str += str(current.data) + "\n"
            # Update the current node
            current = current.next_node
        # Return the list string
        return list_str

