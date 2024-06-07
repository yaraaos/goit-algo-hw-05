def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == x:
            return iterations, arr[mid]
        elif arr[mid] < x:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    return iterations, upper_bound

# Приклад використання
sorted_arr = [1.2, 3.5, 4.7, 6.6, 8.0, 9.1]
x = 5.0
print(binary_search(sorted_arr, x))  # Виведе (кількість ітерацій, 6.6)
