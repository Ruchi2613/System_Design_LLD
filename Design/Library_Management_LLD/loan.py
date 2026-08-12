from datetime import date
from typing import TYPE_CHECKING

# TYPE_CHECKING is used to avoid circular imports during runtime
if TYPE_CHECKING:
    from book_copy import BookCopy
    from member import Member

# Represents a loan transaction for a book copy by a library member
class Loan:
    # Initializes a Loan with a BookCopy and Member, sets checkout date to today
    def __init__(self, book_copy: 'BookCopy', member: 'Member'):
        self.copy = book_copy  # The book copy being loaned
        self.member = member   # The member who borrowed the book copy
        self.checkout_date = date.today()  # The date when the book was checked out

    # Returns the BookCopy associated with this loan
    def get_copy(self) -> 'BookCopy':
        return self.copy

    # Returns the Member associated with this loan
    def get_member(self) -> 'Member':
        return self.member