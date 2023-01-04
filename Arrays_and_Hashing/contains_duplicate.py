'''
Problem: 

Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

'''

class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums) <1 or len(nums) > 10e5:
            return

        for i in nums:
            if i < -10e9 and i > 10e9:
                return

        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False

def main():
    s = Solution()
    
    # move to a unit test to verify the other possible outcomes and corner cases
    print(s.containsDuplicate([1,2,2,4]))
    print(s.containsDuplicate([5,6,8,456,4,1,23]))


if __name__ == "__main__":
    main()

        