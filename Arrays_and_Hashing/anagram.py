'''
Question:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

'''
# solution 1 : won't work in an interview:
# time complexity at best is o(nlogn) - sorting; space complexity is o(1):

# class Solution(object):
#     def isAnagram(self, s, t):
#         return sorted(s) == sorted(t)


# solution 2:
# time complexity is o(n) ; space complexity is o(s + t) // length of the two hashmaps or dict


class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        hashS, hashT = {}, {}

        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i],0)
            hashT[t[i]] = 1 + hashT.get(t[i],0)
        
        for i in hashS:
            if hashS[i] != hashT.get(i,0):
                return False

        return True


def main():
    sol = Solution()
    s = "anagram"
    t = "nagaram"
    print(sol.isAnagram(s,t))

if __name__ == "__main__":
    main()