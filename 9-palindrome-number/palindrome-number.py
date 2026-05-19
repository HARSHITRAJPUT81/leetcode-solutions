class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Negative numbers are not palindrome
        if x < 0:
            return False

        original_number = x
        reverse_number = 0

        # Reverse the number
        while x > 0:

            digit = x % 10

            reverse_number = reverse_number * 10 + digit

            x = x // 10

        # Check both numbers are same or not
        if original_number == reverse_number:
            return True

        return False
        