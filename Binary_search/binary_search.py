'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.

'''


#Solution 1 :
# runtime : 192 ms 
# time complexity o(logn) ; space complexity: o(1) + space for 3 integer variables
# if length 16: then 16 -> 8 -> 4 -> 2 -> 1 : log n (base 2) = x ==> o(n) time complexity
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        firstIndex, lastIndex = 0, len(nums)-1

        while firstIndex <= lastIndex :
            # other languages: if last value is 2^31 (ceil int): adding first will give over flow error ->
            # so another way to calculate mid = first + ((last - first) / 2) -> this will not overflow the variable mid (int)
            midIndex  = int((firstIndex + lastIndex)/2)   # this results in floating midIndex if not type casted
            if nums[midIndex] == target:
                print("target",firstIndex, midIndex, lastIndex)
                return midIndex
            elif target < nums[midIndex]:
                lastIndex = midIndex - 1
                print("target less than mid",firstIndex, midIndex, lastIndex)
            elif target > nums[midIndex]:
                firstIndex = midIndex + 1
                print("target more than mid",firstIndex, midIndex, lastIndex)
        
        return -1


def main():
    sol = Solution()
    result = sol.search([-1,0,3,5,9,12], 2)
    print(result)


if __name__ == "__main__":
    main()