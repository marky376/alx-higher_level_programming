1. How to open a file
In Python, you can use the open() function to open a file. The open() function takes two arguments - the file path and the mode. The mode can be 'r' for reading, 'w' for writing, and 'a' for appending.

# Example: Opening a file for reading
file_path = 'example.txt'
file = open(file_path, 'r')
2. How to write text in a file
To write text to a file, you can use the write() method on the file object.

# Example: Writing text to a file
file.write('Hello, this is a sample text.')
3. How to read the full content of a file
You can use the read() method to read the entire content of a file.

# Example: Reading the full content of a file
content = file.read()
print(content)
4. How to read a file line by line
You can use a for loop to iterate over the file object, which automatically reads the file line by line.

# Example: Reading a file line by line
file_path = 'example.txt'
with open(file_path, 'r') as file:
    for line in file:
        print(line)
5. How to move the cursor in a file
The cursor position in a file is managed automatically, but if you need to move it explicitly, you can use the seek() method.

# Example: Moving the cursor in a file
file.seek(0)  # Move the cursor to the beginning of the file
6. How to make sure a file is closed after using it
You can use the with statement to ensure that a file is closed automatically after its suite finishes.

# Example: Using the with statement to automatically close a file
file_path = 'example.txt'
with open(file_path, 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed outside the 'with' block
7. What is and how to use the with statement
The with statement in Python is used to simplify the management of resources, such as files. It ensures that a resource is properly initialized and finalized. It is commonly used with file handling, database connections, and other resources.

8. What is JSON
JSON (JavaScript Object Notation) is a lightweight data interchange format. It is easy for humans to read and write, and easy for machines to parse and generate. JSON data is represented as key-value pairs similar to Python dictionaries.

9. What is serialization
Serialization is the process of converting a data structure or object into a format that can be easily stored or transmitted, such as JSON.

10. What is deserialization
Deserialization is the process of converting a serialized data format (like JSON) back into its original form, making it usable in a programming language.

11. How to convert a Python data structure to a JSON string
You can use the json.dumps() function to convert a Python data structure to a JSON string.

import json

data = {'name': 'John', 'age': 30, 'city': 'New York'}
json_string = json.dumps(data)
print(json_string)
12. How to convert a JSON string to a Python data structure
You can use the json.loads() function to convert a JSON string back into a Python data structure.

import json

json_string = '{name: John, age: 30, city: New York}'
data = json.loads(json_string)
print(data)
These examples cover the basics of file handling, cursor movement, the with statement, JSON, serialization, and deserialization in Python.
