# Chaabi-Python-Assignment
# Python Practice Questions

This repository contains solutions to various Python practice questions. Each question is implemented as a separate function. Below is a description of each question and its corresponding function.

## Questions

### Q1. Selection Sort Algorithm

Function: `selection_sort(input_list: List[int]) -> List[int]`

Description: Implements the selection sort algorithm to sort a given list in ascending order.

### Q2. File Type Dictionary

Function: `get_file_types(extension_list: str, filenames: List[str]) -> Dict[str, str]`

Description: Given a list of extension and type pairs and a list of filenames, returns a dictionary of filename: type pairs based on the file extension.

### Q3. Column Sorting

Function: `sort_list_of_dicts(data: List[Dict[str, Any]], key: str) -> List[Dict[str, Any]]`

Description: Given a list of dictionaries, sorts the list according to the specified key.

### Q4. Dictionary Key-Value Swap

Function: `swap_dict_keys_values(data: Dict[str, Any]) -> Dict[Any, str]`

Description: Given a dictionary, swaps the keys and values and returns a new dictionary.

### Q5. Common and Not Common Elements

Function: `get_common_and_not_common(list1: List[Any], list2: List[Any]) -> Tuple[List[Any], List[Any]]`

Description: Given two lists, returns the common elements and the elements that are not common between the lists.

### Q6. Sub-list Extraction

Function: `extract_sublist(data: List[Any], start: int, end: int) -> List[Any]`

Description: Given a list and two indices, returns a sub-list containing every second element within the specified indices.

### Q7. Factorial Calculation using Lambda Function

Function: `factorial(n: int) -> int`

Description: Calculates the factorial of a number using a lambda function.

### Q8. Value Analysis

This section provides the final values of variables A0 to A9 based on the given code.

```python
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
A1 = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
A2 = sorted([i for i in A1 if i in A0])  # []
A3 = sorted([A0[s] for s in A0])  # [1, 2, 3, 4, 5]
A4 = [i for i in A1 if i in A3]  # [1, 2, 3, 4, 5]
A5 = {i: i*i for i in A1}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
A6 = [[i, i*i] for i in A1]  # [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
A7 = sum([10, 23, -45, 33])  # 21
A8 = list(map(lambda x: x * 2, [1, 2, 3, 4]))  # [2, 4, 6, 8]
A9 = list(filter(lambda x: len(x) > 3, ["I", "want", "to", "learn", "python"]))  # ['want', 'learn', 'python']
# Python Practice Questions

This repository contains solutions to various Python practice questions. Each question is implemented as a separate function. Below is a description of each question and its corresponding function.

## Questions

### Q9. Date Comparison

Function: `compare_dates(from_date: str, to_date: str, difference: int) -> bool`

Description: Compares two dates and returns True if the difference between them is less than the specified number of days.

### Q10. Date Calculation

Function: `calculate_previous_date(date: str, n: int) -> str`

Description: Given a date in the format 'yy-mm-dd' and a number of days, returns the string representation of the date n days before the input date.

### Q11. Function Execution

Description: The provided code demonstrates the execution of the function `f(x, l=[])`. It appends the square of numbers to a list and prints the list after each function call.



