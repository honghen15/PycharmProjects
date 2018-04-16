class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        flag = False
        max_str = main_max = ''
        text3 = s[0:]
        for index, value in enumerate(s):
            # print(text[index:], end='=')
            # print(text[:-index])
            # print()
            text1 = s[:index + 1]
            len_count1 = int(len(text1) / 2) if len(text1) % 2 == 0 else int(len(text1) / 2) + 1
            for i in range(len_count1):
                # print(text[i], text[len(text)-i-1], end='===\n')
                # if text1[i] == text1[len(text1)-i-1] == ' ':
                #     continue
                if (text1[i] != text1[len(text1) - i - 1]) and flag == True:
                    max_str = ''
                    flag = False
                    # break
                if text1[i] == text1[len(text1) - i - 1]:
                    if (flag == False) and len(max_str) < len(text1[i:len(text1) - i]):
                        max_str = text1[i:len(text1) - i]
                    flag = True
            if max_str != '' and len(main_max) < len(max_str):
                main_max = max_str
            # print(main_max)
            flag = False
            max_str = ''

        for index, value in enumerate(s):
            text2 = s[len(s) - index - 1:]
            len_count2 = int(len(text2) / 2) if len(text2) % 2 == 0 else int(len(text2) / 2) + 1
            for i in range(len_count2):
                # print(text[i], text[len(text)-i-1], end='===\n')
                # if text2[i] == text2[len(text2)-i-1] == ' ':
                #     continue
                if (text2[i] != text2[len(text2) - i - 1]) and flag == True:
                    max_str = ''
                    flag = False
                    # break
                if text2[i] == text2[len(text2) - i - 1]:
                    if (flag == False) and len(max_str) < len(text2[i:len(text2) - i]):
                        max_str = text2[i:len(text2) - i]
                    flag = True
            if max_str != '' and len(main_max) < len(max_str):
                main_max = max_str
            # print(main_max)
            flag = False
            max_str = ''

        return main_max