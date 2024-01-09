A readme file for python input or output Python Read File and Python Write to File
FREE Online Courses: Click, Learn, Succeed, Start Now!

In all your previous programs, you might have dealt with some sort of data. You might have asked the user for some data as input. Your program then might have processed it and produced some output data on the screen. But, one thing worth noticing is that as soon as your program finishes its execution, you lose this data.

In real life applications though, you’ll need to safely store your data somewhere.

In this article, you’ll learn where you can store this data. You’ll learn how you can store, retrieve as well as manipulate this data. In other words, you will learn Python read file, Python write to file, Python open file and python close file.

Keeping you updated with latest technology trends, Join TechVidvan on Telegram

What is Python File?
When we talked about storing our data somewhere, we meant storing our data into files.

A file is a container that stores information, right? In computer systems, a file is a contiguous set of bytes. Data in a computer system is always stored into files. Files can take different forms depending on the user requirements like data files, text files, program executable files etc.

A computer processes these files by translating them into 0s and 1s.

So all the text, images, videos that you store on your computer are nothing but a series of 0s and 1s.

Every file contains three main parts:

1. Header: This contains information about the file i.e. file name, file type, file size etc.
2. Data: This is the actual information/content stored in the file.
3. End of file: This is a special character that marks the end of the file.

Also, in a file, a new line character (‘\n’) marks the end of a line or start of a new line.

Python Open File
You can open file in Python using the built-in function open().

Syntax:

open(filename, access_mode)
Follow TechVidvan on Google & Stay updated with latest technology trends

Parameters
1. filename:

This is the name of the file we want to open. If the file resides in the same directory as your program, you can simply specify the file name. But if the file is not present in the same directory, you need to specify the full path of the file.

2. access_mode:

Access mode specifies what you want to do with the file. The default mode is read mode ‘r’. You’ll find a list of all the access modes later in this article.

Returns
The open() function returns a file object, also called “handle”. Python treats the file as an object and we use this file object in our program to access the contents of the file.

Let’s look at an example.

We have an already existing file in our system – “myfile.txt”. Let’s open this file in the Python shell.

Code:

>>> file_obj = open(myfile.txt, r)   # file in the same directory
>>> file_obj = open(E:/folder/file.txt)  # specify full path if not in the same directory
Python Access Modes
The second argument to open() is the access_mode. The access_mode specifies the mode in which you want to open the file. Modes include “r” for reading, “w” for writing and “a” for appending. This argument is optional and takes the default value of “r”, i.e., the read mode if we pass no value to it.

ModeFunction
rOpen a file for reading. This is the default mode.
wOpen a file for writing. If the file already exists, overwrite its contents. Create a new file if the file does not exist.
aOpen a file for appending. Preserve the file’s contents, add new data to the end of the file.
r+Open a file for reading and writing.
w+Allows to write as well as read from the file.
a+Allows appending as well as reading from the file.
By default, open() function opens a file in text mode.

We can specify binary mode by adding “b” to any of the modes (e.g., “wb” – write to binary data, “rb+” – read and write to binary data).

Python Close File
Many programmers often forget to close a file after they’re done processing it. This may lead to unwanted data loss and data corruption. Closing a file also helps in freeing up all the resources tied to your program for working with the file.

Therefore, it is always a good practice to close your file once you’re done working with it. We do this using a simple in-built Python function – close(). We just need to call the close() method on the file object and Voila! The file is now closed.

No data lost, no resources left still tied to the file.

Code:

>>> file_obj = open(myfile.txt, r)
>>> file_obj.close()
Python Read Data from a File
Let’s now come to the real and fun part: operating on the file.

Python provides us with various functions to read from a file. One way to read individual lines from a file without using any function is by using the “for” loop.

Code:

>>> f = open(myfile.txt)
>>> for line in f:
        print(line)
Output:

Hello world! This is line 1.This is the 2nd line.

And this is line 3.

>>>

This loops over the lines in myfile.txt and prints them one by one.

The functions we have at our disposal to read from python file are:

1. read(size = -1)
This read size number of bytes from the file. If size is not passed, the entire file is read.

Follow along through the session at Python shell.

>>> f.read(5)      # first call
Output:

‘Hello’
>>> f.read(10)     # second call
Output:

‘ world! Th’
>>> f.read()      # third call
Output:

‘is is line 1.\nThis is the 2nd line.\nAnd this is line 3.\n’>>>

The first call to read() reads the first 5 bytes as 5 was passed to the size argument. The second call reads next 10 bytes. And the third call reads the rest of the file as we provide no size argument.

2. readline(size = -1)
This reads size number of bytes from the line. If we pass no argument value, it reads the entire line.

Look at the example code in the Python shell:

>>> f.readline()
Output

‘Hello world! This is line 1.\n’
>>> f.readline()
Output:

‘This is the 2nd line.\n’
>>> f.readline()
Output:

‘And this is line 3.\n’
Notice how the first call to readline returns 1st line, the second call returns 2nd line and so on.

3. readlines()
This function reads all the lines from a file and returns a list of the lines, separating them from one another with commas.

Code:

>>> f.readlines()
Output:

[‘Hello world! This is line 1.\n’, ‘This is the 2nd line.\n’, ‘And this is line 3.\n’]
Python Writing data into a File
Writing into a file is just as easy as reading from it. All we need to do is open a file in write mode.

>>> f = open(myfile.txt , w)
Then the in-built function for writing into the file object will take care of the rest.

1. write(string)
This function takes a string as an argument and writes it into the file. This function returns the number of characters written into the file.

Code:

>>> f.write(I am writing new text into the filen)
Output:

37
2. writelines(list_of_strings)
This function takes a list of strings as an argument and writes those strings into the file. Be sure to append a “\n” at the end of a string to make it act as a line. The function does not append any line endings to the elements of the list of strings.

Code:

>>> lines = [Second linen, Third linen, Fourth linen]
>>> f.writelines(lines)
>>> f.close()
Once you close the file, all changes get committed to it.

You can see the changes in the file:

python alter file

Python File Pointer Position
Python provides us with 2 in-built methods when it comes to working with the file pointer.

1. tell()
The tell() method returns the current position of the file pointer. That is, it returns the number of bytes from the beginning of the file.

2. seek(offset, whence)
The seek method lets you control the position of the file pointer. This method takes two parameters:

a. offset – The number of positions(bytes) to move forward.

b. whence – This is optional. This denotes the position from where you want to move forward. It can take three values:

0: move forward from the start of the file.
1: seek relative to the current position.
2: move backwards from the end of the file.
Now, look at this session of Python shell.

>>> f.readline()
Output:

‘I am writing a new line to the file \n’
>>> f.tell()
Output:

38
>>> f.seek(20)
Output:

20
>>> f.tell()
Output:

20
>>> f.read()
Output:

‘ine to the file \nSecond line\nThird line\nFourth line\n’>>>

Python File Methods
MethodWhat it does
close()Closes the file.
flush()Flushes the internal buffer.
fileno()Returns the file descriptor of the file.
next()Returns the next line from the file.
read(size)Reads size number of bytes from the file. Reads the entire file if you don’t pass any argument value.
readline(size)Reads one line from a file. 
readlines()Reads the entire file and returns a list of the lines.
seek(offset, whence)Lets us control the position of the file pointer.
tell()Returns the current position of the file pointer.
truncate(size)It truncates the file to the specified size.
writable()Returns True if we can write into the file.
write(string)Writes string into the file.
writelines(list_of_strings)Writes each element of the list_of_strings into the file.
Summary
In this article, we learned what files are and how we can access and manipulate them. We saw Python read file, write file, Open file and close file.

Storing your program’s data into a file increases the application and usability of your program. The utility of your application is also increased when you are able to get data from a file into your program. Now that you know how to work with files (open, process and close them), you can build better programs.
