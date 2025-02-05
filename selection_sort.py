def selection_sort(nums):
    for i in range(0, len(nums)):
        idx = i
        for j in range(idx+1, len(nums)):
            if nums[j] < nums[idx]:
                idx = j
        nums[i], nums[idx] = nums[idx], nums[i]
    return nums

result = selection_sort([9, 6, 2, 1, 8, 7])
print(result)

