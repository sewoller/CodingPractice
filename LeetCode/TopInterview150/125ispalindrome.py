import re

def isPalindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    #convert to lowercase, remove non-letter characters
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    if len(s) < 1:
        return True

    low, high = 0, len(s)-1
    while s[low] == s[high]:
        low += 1
        high -= 1
        if low >= high:
            return True
    
    return False
    

input = "A man, a plan, a canal: Panama"

print(isPalindrome(input))