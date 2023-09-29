#My way to solve this problem
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for index_of_num1, num1 in enumerate(nums):
            for index_of_num2, num2 in enumerate(nums):
                if index_of_num1 == index_of_num2:
                    continue
                else:
                    if num1 + num2 == target:
                        print(f"[{index_of_num1}, {index_of_num2}]")
                        exit()


object = Solution()
result = object.twoSum([2, 7, 11, 15], 9)

print(result)

# Better solution
# class Solution(object):
#     def twoSum(self, nums, target):
#         num_dict = {}
#
#         for index, num in enumerate(nums):
#             complement = target - num
#
#             if complement in num_dict:
#                 return [num_dict[complement], index]
#
#             num_dict[num] = index
#
# object = Solution()
# result = object.twoSum([2, 7, 11, 15], 9)
#
# print(result)