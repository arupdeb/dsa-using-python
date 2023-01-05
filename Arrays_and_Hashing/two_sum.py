'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

# solution 1:
# time complexty is o(n2) space complexity is o(1)

# class Solution(object):
#     def twoSum(self, nums, target):
#         if len(nums) < 2:
#             return {}
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return {i,j}


# solution 2:
# time complexity is o(n) : space complexity is o(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        previousElementHash = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in previousElementHash:
                return {i, previousElementHash[diff]}
            previousElementHash[nums[i]] = i

        return


def main():
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))


if __name__ == "__main__":
    main()
