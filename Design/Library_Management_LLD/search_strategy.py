from abc import ABC, abstractmethod
from typing import List
from library_item import LibraryItem

class SearchStrategy(ABC):
    @abstractmethod
    def search(self, query: str, items: List[LibraryItem]) -> List[LibraryItem]:
        pass

class SearchByTitleStrategy(SearchStrategy):
    def search(self, query: str, items: List[LibraryItem]) -> List[LibraryItem]:
        result = []

        for item in items: 
            title = item.get_title()

            if query.lower() in title.lower():  
                result.append(item) 

        return result

class SearchByAuthorStrategy(SearchStrategy):
    def search(self, query: str, items: List[LibraryItem]) -> List[LibraryItem]:
        result = []

        for item in items:
            author = item.get_author_or_publisher()

            if query.lower() in author.lower():
                result.append(item)

        return result