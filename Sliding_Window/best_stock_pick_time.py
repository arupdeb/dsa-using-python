'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

Test cases:
[7,1,5,3,6,4] : 5
[7,6,4,3,1] : 0
[2,4,1] : 2
[2,1,2,0,1] :  1
[3,2,6,5,0,3] : 4
[4,1,2] : 1
[2,7,1,4] : 5 

'''

# solution 1: using two pointer method
# time complexity o(n) ; space complexity o(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        first , last = 0, 1 
        maxprofit = 0

        while last < len(prices):
            if prices[first] < prices[last]:
                maxprofit = self.maxProfitCalc(maxprofit, prices[last] - prices[first])
            else:
                first = last

            last+=1 

        return maxprofit

    def maxProfitCalc(self, value1, value2):
        if value1 > value2 :
            return value1
        else:
            return value2


            
def main():
    sol = Solution()
    result = sol.maxProfit([7,1,5,3,6,4])
    print(result)


if __name__ == "__main__":
    main()


