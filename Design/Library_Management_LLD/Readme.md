Order	File Name	Depends On	Why Create First? / What It Does
1	item_type.py	None	Enum for item types (Book, Magazine, etc.)
2	item_states.py	None	Defines states (Available, CheckedOut, etc.)
3	library_item.py	item_type.py	Base class for all items, uses item_type
4	book_copy.py	library_item.py, item_states.py	Physical copy, uses states, item
5	member.py	library_item.py	Member class, may reference items
6	item_factory.py	item_type.py, library_item.py	Creates items, uses item_type and item
7	search_strategy.py	library_item.py	Search logic, uses library items
8	library_management_system.py	All above files	Main manager, uses all above files
9	demo file (main.py)	library_management_system.py, etc	Entry point, uses manager and others