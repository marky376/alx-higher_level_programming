#!/usr/bin/python3
"""a function that prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """
    Print the text with 2 new lines after each occurrence of '.', '?', or ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If the input text is not a string.

    Returns:
        None

    Example:
        >>> text_indentation("Hello. This is a sample text. How are you doing?")
        Hello.
        This is a sample text.
        How are you doing?
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()

    if not text:
        return

    result = ""
    for char in text:
        result += char
        if char in ['.', '?', ':']:
            print(result.strip())
            print()
            result = ""

    if result:
        print(result.strip())
