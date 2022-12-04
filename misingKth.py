# def findKthPositive(arr, k):
#     last_num = 0
#     k_at = 0
#
#     for num in arr:
#         diff = num - last_num - 1
#         if k_at + diff >= k:
#             return last_num + (k - k_at)
#         last_num = num
#         k_at += diff
#     return arr[-1] + (k - k_at)
#
#
# arr = [2, 3, 4, 7, 11]
# k = 5
# print(findKthPositive(arr, k))
# print("a"<"c")