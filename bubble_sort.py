def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping:
        for i in range(1, end):
            if nums[i - 1] < nums[i]:
                temp = nums[i - 1]
                nums[i - 1] = nums[i]
                nums[i] = temp
                swapping = False
        end -= 1
    

input = [5, 4, 3, 2, 1]
result = bubble_sort(input)
print(result)    

