from library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, item_id: str, title: str, author: str):
        super().__init__(item_id, title)
        self.author = author

    def get_author_or_publisher(self) -> str:
        return self.author
    
    '''Explanation for beginners:
    LibraryItem → Parent class

    Book → Child class that means Book inherits things from LibraryItem. and A Book is also a Library Item.
    
    2. What is super()?: Call the parent class method. It means:

 Run the constructor (__init__) of the parent class (LibraryItem). 
 
 
    3. Why Do We Use It?

    Because the parent class already has some code we want to reuse.

    Instead of writing the same code again, we call the parent.

    This is called code reuse.
    
    4. Example Parent Class

    Suppose LibraryItem looks like this:

    class LibraryItem:
        def __init__(self, item_id, title):
            self.item_id = item_id
            self.title = title

    This class stores:

    item_id,
    title

    5. Now Look at Your Code
    class Book(LibraryItem):
    def __init__(self, item_id: str, title: str, author: str):
        super().__init__(item_id, title)
        self.author = author
    ---step by step:

    Step 1

    When you create a Book:

    book = Book("B1", "Harry Potter", "J.K. Rowling")

    Step 2

    Python enters this constructor:

    __init__(item_id, title, author)

    Values:

    item_id = B1
    title = Harry Potter
    author = J.K. Rowling


    Step 3

    This line runs:

    super().__init__(item_id, title)

    It calls LibraryItem constructor.


    So this runs:

    self.item_id = item_id
    self.title = title

    Now the book object has:

    item_id = B1
    title = Harry Potter

    Step 4

    Then this line runs:

    self.author = author

    Now the object has:

    item_id = B1
    title = Harry Potter
    author = J.K. Rowling


    ----- 
    6. Without super() (Problem)

    If we didn't use super():

    class Book(LibraryItem):
        def __init__(self, item_id, title, author):
            self.author = author

    Then the object would not have:

    item_id
    title

    Because the parent constructor never ran.

    Real Life Example

    Think like this:

    Parent class: Vehicle

    Vehicle
    - engine
    - wheels

    Child class: Car

    Car
    - engine
    - wheels
    - doors

    Using super():

    Vehicle sets engine and wheels
    Car adds doors


    therefore: super() means:

 Call the parent class method
 Reuse parent code
 Avoid rewriting code
 Important for inheritance


 so, Your code simply means:

Book inherits from LibraryItem
LibraryItem sets item_id and title
Book adds author

        '''
