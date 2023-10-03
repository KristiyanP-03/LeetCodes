class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        last_opening_brackets = []
        brackets_map = {
            '(': ')',
            '{': '}',
            '[': ']',
        }


        for bracket in s:
            if bracket in brackets_map.keys():
                last_opening_brackets.append(bracket)
                continue


            elif bracket in brackets_map.values():
                if not last_opening_brackets:
                    return False

                needed_opening_bracket = [key for key, value in brackets_map.items() if value == bracket][0]


                if last_opening_brackets[-1] == needed_opening_bracket:
                    last_opening_brackets.pop()
                else:
                    return False


        else:
            if not last_opening_brackets:
                return True







object = Solution()

output = object.isValid("([)")

print(output)