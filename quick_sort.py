def quick_sort(nums, low, high):
    if low < high:
        index = partition(nums, low, high)
        quick_sort(nums, low, index-1)
        quick_sort(nums, index+1, high)

def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i


lst = [9, 6, 2, 1, 8, 7]
quick_sort(lst, 0, len(lst) - 1)
print(lst)

