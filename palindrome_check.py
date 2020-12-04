def isPalindrome(string):
    # two pointers
    # one variable starting at beginning of string
    # the other at the end of string
    # while left < right:

    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

