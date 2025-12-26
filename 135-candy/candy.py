class Solution:
    def candy(self, ratings: List[int]) -> int:
        r = len(ratings)
        candy = [1] * r
        total = 0
        #Left to right. Ignore 0, but do r-1
        for i in range(1, r):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        #Right to left. Do 0, but ignore r-1
        for i in range(r-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i], candy[i+1] + 1)
        total = sum(candy)
        return total