def singleNonDuplicate(nums):
    start = 0
    end = len(nums) - 1
    while start < end:
        mid = (start+end)//2
        if (mid % 2 == 1 and nums[mid-1] == nums[mid]) or (mid %2 == 0 and nums[mid] == nums[mid+1]):
            start = mid + 1
        else:
            end = mid
    return nums[start]


nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
print(singleNonDuplicate(nums))
