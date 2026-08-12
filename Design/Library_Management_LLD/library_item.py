from abc import ABC, abstractmethod
from typing import List, Optional
from member import Member
from book_copy import BookCopy

class LibraryItem(ABC):
    def __init__(self, item_id: str, title: str):
        # Unique identifier for the item (e.g., ISBN for books)
        self.id = item_id
        # Title of the item (e.g., book title)
        self.title = title
        # List to store all physical copies of this item
        # Example: [BookCopy('B1-c1', self), BookCopy('B1-c2', self)]
        self.copies: List['BookCopy'] = []
        # List to store all members who are waiting for this item (Observer pattern)
        # Example: [Member('M1', 'Alice'), Member('M2', 'Bob')]
        self.observers: List[Member] = []

    def add_copy(self, book_copy: 'BookCopy') -> None:
        # Add a new physical copy to the list
        self.copies.append(book_copy)
        # Now self.copies contains all BookCopy objects for this item

    def add_observer(self, member: Member) -> None:
        # Add a member to the observers list (waiting for this item)
        self.observers.append(member)
        # Now self.observers contains all Member objects waiting for this item

    def remove_observer(self, member: Member) -> None:
        # Remove a member from the observers list if present
        if member in self.observers:
            self.observers.remove(member)

    def notify_observers(self) -> None:
        print(f"Notifying {len(self.observers)} observers for '{self.title}'...")
        # Iterate over a copy of the observers list to avoid modification during iteration
        for observer in self.observers.copy():
            observer.update(self)

    def get_available_copy(self) -> Optional['BookCopy']:
        # Return the first available copy from the list
        for book_copy in self.copies:
            if book_copy.is_available():
                return book_copy
        return None

    def get_id(self) -> str:
        # Return the unique ID of the item
        return self.id

    def get_title(self) -> str:
        # Return the title of the item
        return self.title

    def get_copies(self) -> List['BookCopy']:
        # Return the list of all physical copies
        return self.copies

    @abstractmethod
    def get_author_or_publisher(self) -> str:
        # Abstract method to get author or publisher (implemented in subclasses)
        pass

    def get_available_copy_count(self) -> int:
        # Return the number of available copies
        return sum(1 for book_copy in self.copies if book_copy.is_available())

    def has_observers(self) -> bool:
        # Return True if there are any observers waiting for this item
        return len(self.observers) > 0

    def is_observer(self, member: Member) -> bool:
        # Return True if the given member is in the observers list
        return member in self.observers

# Example of how lists work:
# self.copies = [BookCopy('B1-c1', self), BookCopy('B1-c2', self)]
# self.observers = [Member('M1', 'Alice'), Member('M2', 'Bob')]
# You can add, remove, and iterate over these lists.

# For dictionaries, you would use: self.catalog = {'B1': LibraryItem(...), 'B2': LibraryItem(...)}
# Where keys are item IDs and values are LibraryItem objects.