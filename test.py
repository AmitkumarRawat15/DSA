def nextGreatestLetter(letters, target):
    # left = 0
    # right = len(letters)
    # middle = int((left + right) / 2)
    # while left < right:
    #     if letters[middle] > target:
    #         right = middle - 1
    #     else:
    #         left = middle + 1
    #     middle = int((left + right) / 2)
    # if middle == len(letters) - 1 or middle == len(letters) or middle == -1:
    #     return letters[0]
    # elif letters[middle] <= target:
    #     return letters[middle + 1]
    # else:
    #     return letters[middle]
        start = 0
        end = len(letters)
        mid = (start + end)//2
        while start < end:
            if letters[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
            mid = (start + end)//2
            if mid == len(letters) - 1 or mid == len(letters) or mid == -1:
                return letters[0]
            elif letters[mid] <= target:
                return letters[mid + 1]
            else:
                return letters[mid]


letters = ["c", "f", "j"]
target = "a"
print(nextGreatestLetter(letters, target))