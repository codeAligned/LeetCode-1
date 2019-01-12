# 273. Integer to English Words
# Time:  O(1)
# Space: O(1)

# split them three digits as a group
class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: # special case 0
            return "Zero"
        
        under_twenty_mapping = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
        tens_mapping = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}
        billion_num = num // 10**9
        million_num = (num % 10**9) // 10**6
        thousand_num = (num % 10**6) // 10**3
        leftover_num = num % 10**3
        
        def numToWords(num):
            word = ''
            hundred_num = num // 10**2
            if hundred_num > 0:
                word += under_twenty_mapping[hundred_num] + ' Hundred '
            tens_num = num % 10**2
            if 0 < tens_num < 20:
                word += under_twenty_mapping[tens_num]
            elif tens_num >= 20:
                ten_digit = tens_num // 10
                word += tens_mapping[ten_digit]
                unit_digit = tens_num % 10
                if unit_digit > 0:
                    word += ' ' + under_twenty_mapping[unit_digit]
            
            return word.strip()
        
        res = ''
        if billion_num > 0:
            res += numToWords(billion_num) + ' Billion ' 
        if million_num > 0:
            res += numToWords(million_num) + ' Million '
        if thousand_num > 0:
            res += numToWords(thousand_num) + ' Thousand '
        if leftover_num > 0:
            res += numToWords(leftover_num)
        
        return res.strip()
