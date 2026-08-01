class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x<0:
            return False
        num = x
        palindrome__number = 0
        while num> 0:
            id = num%10
            palindrome__number = (palindrome__number*10)+id
            num = num//10
        return x == palindrome__number
        