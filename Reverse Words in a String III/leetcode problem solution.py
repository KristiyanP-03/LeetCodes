class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_string = ""
        string_separate_by_white_spaces = s.split(" ")


        for word in string_separate_by_white_spaces:
            word = word[::-1]

            new_string += word + " "

        return new_string[:len(new_string)-1:]

object = Solution()

output = object.reverseWords("God Ding")

print(output)