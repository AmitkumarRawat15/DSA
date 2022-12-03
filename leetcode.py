def intersection(nums1, nums2):
    result = []
    if len(nums1) == 0 or len(nums1) == 0:
        return result
    num1.sort()
    num2.sort()

    len1 = len(nums1)
    len2 = len(nums2)
    i1 = 0
    i2 = 0
    while i1 < len1 and i2 < len2:
        if nums1[i1] == nums2[i2]:
            if nums1[i1] not in result:
                result.append(nums1[i1])
                i1 += 1
                i2 += 1
        elif nums1[i1] > nums2[i2]:
            i2 += 1
        else:
            i1 += 1
    return result


num1 = [4, 9, 5]
num2 = [9, 4, 9, 8, 4]
print(intersection(num1, num2))
