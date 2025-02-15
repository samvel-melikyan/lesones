from lesones.functions.functions import *
new_section("search")
line("Binary search")
short_line("Логарифмическая сложность  O(log n)")
print("""
Алгоритм бинарного поиска — это такой алгоритм, который 
позволяет найти элемент уже в отсортированном списке.""")

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None







