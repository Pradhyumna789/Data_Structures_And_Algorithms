def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if lst[mid] == target:
            return f"target found at index {mid}"
        elif lst[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1


target = 42
result = binary_search([1, 7, 12, 13, 30, 42, 54, 71, 99], target)
print(result)

