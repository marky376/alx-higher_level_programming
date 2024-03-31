1. **Fetching internet resources with the Python package urllib:**
   - `urllib` is a Python library that allows you to make HTTP requests and interact with web resources.
   - It provides several modules such as `urllib.request` for opening and reading URLs and `urllib.parse` for parsing URLs.
   - Basic usage involves using `urllib.request.urlopen()` to open a URL and then reading the response with `.read()`.

2. **Decoding urllib body response:**
   - After fetching a response with `urllib`, the data obtained is often in bytes format.
   - Decoding involves converting these bytes into a human-readable format, typically using the `.decode()` method with an appropriate character encoding like UTF-8.

3. **Using the Python package requests:**
   - `requests` is a third-party library that simplifies making HTTP requests compared to `urllib`.
   - It provides a higher-level interface and is generally easier to use and more feature-rich.
   - Basic usage involves importing the library and then using functions like `requests.get()` or `requests.post()` to make various types of HTTP requests.

4. **Making HTTP GET request:**
   - An HTTP GET request is used to retrieve data from a specified resource.
   - In Python using `requests`, you can make a GET request by calling `requests.get()` and passing the URL as an argument.

5. **Making HTTP POST/PUT/etc. request:**
   - HTTP POST, PUT, DELETE, etc., are used to send data to a server to create or modify a resource.
   - In Python using `requests`, you can make these requests using `requests.post()`, `requests.put()`, `requests.delete()`, etc., by passing data along with the request.

6. **Fetching JSON resources:**
   - JSON (JavaScript Object Notation) is a lightweight data interchange format.
   - Many web APIs provide data in JSON format.
   - To fetch JSON resources in Python using `requests`, you make a request and then use the `.json()` method on the response object to decode the JSON data into a Python dictionary.

7. **Manipulating data from an external service:**
   - This involves fetching data from an external source, such as a web API, and then processing or using that data in your application.
   - Once you've fetched the data, you can manipulate it in various ways, such as filtering, sorting, transforming, or analyzing it to extract insights.
