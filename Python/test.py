# nums = [2, 1, 4, 3, 1, 0, 8, 3, 5, 2, 7, 4, 1, 3, 2]
# k = 3

# def rotate(nums, k):
#     n = len(nums)
#     k = k % n
#     if k == 0: return

#     temp = nums[-k:]
#     # print(nums)
#     nums[k:] = nums[:-k]
#     # print(nums)
#     nums[:k] = temp


# def rotate2(nums, k):
#     def reverse(arr, start, end):
#         x = end
#         for i in range(start, (start+end)//2+1):
#             arr[i], arr[x] = arr[x], arr[i]
#             x = x -1
#         return arr

#     nums = nums[::-1]
#     nums = reverse(nums, 0, k-1)
#     nums = reverse(nums, k, len(nums)-1)
#     print(nums)


# def trap(height) -> int:
#     left = 0
#     right = len(height) - 1
#     left_max = height[left]
#     right_max = height[right]
#     water = 0
#     while left<right:
#         print(left_max, right_max)
#         if left_max < right_max:
#             left += 1
#             print("left ", height[left])
#             left_max = max(left_max, height[left])
#             water += left_max - height[left]
#         else:
#             right -= 1
#             print("right ", height[right])
#             right_max = max(right_max, height[right])
#             water += right_max - height[right]
#         print("water ", water)
#     return water

# #rotate2(nums, k)
# print(trap(nums))


d = {1:'s', 2:'d'}
print(d)
d.pop(5)
print(d)