numbers = [10, 5, 8, 2, 7]
numbers2 = [3, 6, 9, 1, 4]
numbers3 = [11, 4, 5, 6, 8]
numbers4 = [1, 3, 4, 6, 7]
numbers5 = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 7, 10]

print(len(numbers), "Len") # Number of numbers
print(max(numbers), "Max") # Max number
print(min(numbers), "Min") # Min number
print(sum(numbers), "Sum") # Total sum of numbers
print(sorted(numbers), "Sorted") # Organize the list
print(list(enumerate(numbers)), "Enumerate") # Show index and value

print(list(reversed(numbers)), "Reversed") # Reverse the list

numbers.reverse() # Reverse the list option 2
print(numbers, "Reversed Option 2")

numbers.extend(numbers2)
numbers.sort()
print(numbers, "Extended and Sorted")

# zip will only pair up to the length of the shorter list (numbers4)
print(list(zip(numbers3, numbers4)), "Zipped")

numbers.insert(3, 99)
print(numbers, "Inserted 99 at Index 3")

numbers.append(100)
print(numbers, "Appended 100 at the end")

numbers.remove(9)
print(numbers, "Removed 9")

numbers.pop()
numbers.pop(2)
print(numbers, "Popped Index 2 and the last Index")

print(numbers.index(99), "Returns index of the value 99")

print(numbers5.count(6), "Returns count of the value 6")

numbers.clear()
print(numbers, "Cleared all elements")