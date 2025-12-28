class Solution:
    #count possibles up to n
    def count_till_n(self,n):
        s = str(n)

        @cache
        def recursive(ind,diff,tight):
            if ind == len(s) : return 1 if diff == 0 else 0
            #max digit that can be placed without going over
            max_digit = int(s[ind]) if tight else 9
            
            res = 0
            #loop through digits
            for digit in range(max_digit+1):
                #nes difference between odd and even places
                new_diff = diff + (digit if ind%2 else -1*digit)
                new_tight = (digit == max_digit) and tight

                res += recursive(ind+1,new_diff,new_tight)
            return res
        #start with first digit
        return recursive(0,0,True)
    def countBalanced(self, low: int, high: int) -> int:
        return self.count_till_n(high) - self.count_till_n(low-1)