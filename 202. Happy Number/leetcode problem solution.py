class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def get_next_number(num):
            current_last_sum = 0
            while num > 0:
                digit = num % 10
                current_last_sum += digit * digit
                num //= 10
            return current_last_sum

        seen_numbers = set()
        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = get_next_number(n)

        return n == 1





object = Solution()

output = object.isHappy(2)

print(output)