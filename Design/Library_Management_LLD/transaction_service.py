from typing import Dict, Optional, TYPE_CHECKING
from loan import Loan

if TYPE_CHECKING:
    from book_copy import BookCopy
    from member import Member


class TransactionService:

    _instance: Optional['TransactionService'] = None # This means _instance may contain a TransactionService object or None. and This is used to implement the Singleton Design Pattern. Meaning:There should be only one TransactionService object in the entire system.


    def __init__(self):
        if TransactionService._instance is not None:#This prevents creating multiple objects.
            raise Exception("This class is a singleton!") # if and an instance already exists, the program throws an exception.
        self.active_loans: Dict[str, Loan] = {} #This dictionary stores all active book loans.

  
    @staticmethod
    def get_instance() -> 'TransactionService':
        if TransactionService._instance is None: #If the instance doesn't exist → create one.
            TransactionService._instance = TransactionService()
        return TransactionService._instance#Always return the same instance.


    def create_loan(self, book_copy: 'BookCopy', member: 'Member') -> None:
        if book_copy.get_id() in self.active_loans: # This method runs when a member borrows a book.
            raise ValueError("This copy is already on loan.") # If the book copy already exists in active_loans, it means someone already borrowed it, so an error is raised. 
        
        loan = Loan(book_copy, member) # loan = Loan(book_copy, member)
        self.active_loans[book_copy.get_id()] = loan # self.active_loans[book_copy.get_id()] = loan
        member.add_loan(loan) # member.add_loan(loan) The member object also stores the loan in their personal loan list. Member loans = [Loan1, Loan2]

    
    def end_loan(self, book_copy: 'BookCopy') -> None: #. This method runs when the book is returned.
        loan = self.active_loans.pop(book_copy.get_id(), None) # pop() removes the entry and returns the loan.
        if loan is not None:
            loan.get_member().remove_loan(loan) # This removes the loan from the member’s loan list.