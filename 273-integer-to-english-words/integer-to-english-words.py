class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        bel20 = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
            "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]

        tens = [
            "", "Ten", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return bel20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return bel20[n // 100] + " Hundred " + helper(n % 100)

        res = ""

        if num >= 1000000000:
            res += helper(num // 1000000000) + "Billion "
            num %= 1000000000

        if num >= 1000000:
            res += helper(num // 1000000) + "Million "
            num %= 1000000

        if num >= 1000:
            res += helper(num // 1000) + "Thousand "
            num %= 1000

        res += helper(num)

        return res.strip()