# Define a class named Square
class Square:
    # Define a private instance attribute named size
    __size = 0
    # Define a private instance attribute named position
    __position = (0, 0)

    # Define a constructor method that takes two optional arguments, size and position
    def __init__(self, size=0, position=(0, 0)):
        # Assign the arguments to the private attributes using the setters
        self.size = size
        self.position = position

    # Define a property getter for the size attribute
    @property
    def size(self):
        # Return the value of the private attribute size
        return self.__size

    # Define a property setter for the size attribute
    @size.setter
    def size(self, value):
        # Check if the value is an integer, otherwise raise a TypeError exception
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        # Check if the value is less than 0, otherwise raise a ValueError exception
        if value < 0:
            raise ValueError("size must be >= 0")
        # Assign the value to the private attribute size
        self.__size = value

    # Define a property getter for the position attribute
    @property
    def position(self):
        # Return the value of the private attribute position
        return self.__position

    # Define a property setter for the position attribute
    @position.setter
    def position(self, value):
        # Check if the value is a tuple of 2 positive integers, otherwise raise a TypeError exception
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        # Assign the value to the private attribute position
        self.__position = value

    # Define a public instance method named area that returns the current square area
    def area(self):
        # Return the value of the size raised to the power of 2
        return self.__size ** 2

    # Define a public instance method named my_print that prints the square with the character #
    def my_print(self):
        # Check if the size is 0, then print an empty line
        if self.__size == 0:
            print()
        # Otherwise, print the square according to the position and size
        else:
            # Print new lines for the vertical position
            print("\n" * self.__position[1], end="")
            # Loop through the size
            for i in range(self.__size):
                # Print spaces for the horizontal position
                print(" " * self.__position[0], end="")
                # Print hashes for the square
                print("#" * self.__size)
    # Define a special method named __str__ that returns a string representation of the square
    def __str__(self):
        # Initialize an empty string to store the square representation
        square_str = ""
        # Check if the size is 0, then return an empty string
        if self.__size == 0:
            return square_str
        # Otherwise, add the square to the string according to the position and size
        else:
            # Add new lines for the vertical position
            square_str += "\n" * self.__position[1]
            # Loop through the size
            for i in range(self.__size):
                # Add spaces for the horizontal position
                square_str += " " * self.__position[0]
                # Add hashes for the square
                square_str += "#" * self.__size
                # Add a new line after each row
                square_str += "\n"
            # Remove the last new line from the string
            square_str = square_str[:-1]
            # Return the square string
            return square_str

