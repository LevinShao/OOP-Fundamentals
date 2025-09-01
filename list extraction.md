Extracting values from a list in Python can be achieved using several methods, depending on whether single or multiple elements are needed and if any conditions apply.
1. Accessing Single Elements by Index:
Individual elements are retrieved using their zero-based index within square brackets.
list[0] extracts the first element, list[1] extracts the second, and so on.
Negative indices count from the end of the list; list[-1] extracts the last element.
Example:

Python

my_list = [10, 20, 30, 40, 50]
first_element = my_list[0]
last_element = my_list[-1]
print(f"First element: {first_element}")
print(f"Last element: {last_element}")

2. Slicing to Extract Multiple Elements:
Slicing extracts a sub-list (a range of elements) using the syntax list[start:end].
The element at the end index is not included in the result.
Omitting start defaults to the beginning of the list, and omitting end defaults to the end.
Example:

Python

my_list = [10, 20, 30, 40, 50]
sub_list = my_list[1:4] # Extracts elements from index 1 up to (but not including) index 4
print(f"Sub-list: {sub_list}")

3. List Comprehension for Conditional Extraction:
List comprehensions provide a concise way to create new lists by iterating over an existing list and applying a condition.
Example:
Python

my_list = [10, 20, 30, 40, 50]
filtered_elements = [x for x in my_list if x > 25]
print(f"Filtered elements: {filtered_elements}")
4. Using filter() Function:
The filter() function extracts elements based on a function that returns True or False for each item.
Example:
Python

my_list = [10, 20, 30, 40, 50]
filtered_elements_filter = list(filter(lambda x: x > 25, my_list))
print(f"Filtered elements (using filter): {filtered_elements_filter}")
5. Using pop() to Extract and Remove:
The pop() method extracts an element at a specified index and simultaneously removes it from the list.
Example:
Python

my_list = [10, 20, 30, 40, 50]
extracted_and_removed = my_list.pop(2) # Extracts and removes element at index 2 (30)
print(f"Extracted and removed element: {extracted_and_removed}")
print(f"List after pop: {my_list}")