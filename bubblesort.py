def bubble_sort(nums):
    for i in range(len(nums)-1):
        swapped = False
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums


nums = [89, 43, 84, 90, 25, 12, 45]
print(bubble_sort(nums))
