# Problem available at:  https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3353/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
                
        change_method_count = [1] + [ 0 for _ in range(amount)]
        
        for cur_coin in coins:
            
            # update change method count from small amount to large amount
            for small_amount in range(cur_coin, amount+1):
                
                # current small amount can make changed with current coin
                change_method_count[small_amount] += change_method_count[small_amount - cur_coin]
                
        return change_method_count[amount]
        
            
