# def palindrome(s):
#     res = ""
#     resLen = 0
#     for i in range(len(s)):
#         l, r = i, i`
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             if(r-l+1) > resLen:
#                 res = s[l:r+l]
#                 resLen = r - l + 1
#             l-=1
#             r+=1
#
#         # l, r = i, i+1
#         # while l>=0 and r<len(s) and s[l]==s[r]:
#         #     if(r-l+1)> resLen:
#         #         res = s[l:r+l]
#         #         resLen = r - l + 1
#         #     l-=1
#         #     r+=1
#     return res
#
# s = "babad"
# print(palindrome(s))
