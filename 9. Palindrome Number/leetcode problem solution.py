class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        #My solution with converting to string
        # string = str(x)
        #
        # if string == string[::-1]:
        #     return True
        # else:
        #     return False


        #My solution without converting to string
        a = 0
        c = x
        while x > 0:
            r = x % 10
            x = x // 10
            a = (10 * a) + r
        if a == c:
            return True
        else:
            return False


object = Solution()

output = object.isPalindrome(121)

print(output)