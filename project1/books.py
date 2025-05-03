  # creating fastapi application
from fastapi import FastAPI

app = FastAPI()  

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get("/books")
def read_all_books():
    return BOOKS
  

@app.get("/books/mybook")
async def read_all_books():
  return {"Answer":"My Favorite book"}



@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
  for book in BOOKS:
    if book.get('title').casefold() == book_title.casefold():
      return book

@app.get("/books/")
async def read_category_by_query(category: str):
  books_to_return = []
  for book in BOOKS:
    if book.get('category').casefold() == category.casefold():
      books_to_return.append(book)
      
  return books_to_return


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str,category: str):
  books_to_return = []
  for book in BOOKS:
    if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
      books_to_return.append(book)
      
  return books_to_return
    
  
# https://example.com/my%20file
  
# The %20 represents a space between “my” and “file” in the URL. It’s common to see this kind of 
# encoding when handling URLs that contain spaces or special characters.


# In FastAPI, path parameters are dynamic values that you can extract from the URL path. They are a key feature in defining APIs that need to handle varying data in the URL. For example, in a URL like /items/{item_id}, the {item_id} part is a path parameter, and you can use it to capture the value passed in that part of the URL.

# Basic Syntax:
  
  
# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     return {"item_id": item_id}
  
  
# In this example:
# 	•	The URL /items/42 would call read_item(42).
# 	•	The parameter item_id is extracted from the URL and passed to the function as an argument.

# Steps for Understanding Path Parameters:
# 	1.	Define Path Parameter in the URL:
# Path parameters are written inside curly braces {} in the route path.
# 	2.	Use the Path Parameter in the Function:
# Once you define the parameter in the path, you simply declare it as a function argument with the same name as the placeholder in the path.
# 	3.	FastAPI Automatically Handles Type Conversion:
# FastAPI will automatically convert the path parameter to the correct type as defined in the function signature. If you define item_id: int, FastAPI will automatically convert the path parameter to an integer.
