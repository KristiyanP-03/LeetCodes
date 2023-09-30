class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        total_value = 0

        roman_nums_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }



        prev_value = 0

        for char in s[::-1]:
            current_value = roman_nums_dict[char]


            if current_value < prev_value:
                total_value -= current_value
            else:
                total_value += current_value

            prev_value = current_value




        return total_value




object = Solution()
output = object.romanToInt("MCMXCIV")
print(output)