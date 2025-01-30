palindrome = "bbbb"
print(len(palindrome))

def longestPalindrome(s: str) -> str:
    print("input: ", s)
    if len(s) <= 1:
        return s
    longest = s[0]
    for i in range(1, len(s)):
        print("middle: ", s[i])
        left, right = i-1, i+1
        print("Testing with middle letter, ", left, right)
        while left >= 0 and right < len(s) and s[left] == s[right] :
            print("new pal: ", s[left:right+1])
            if len(longest) < len(s[left:right+1]):
                longest = s[left:right+1]
                print("longest: ", longest)
            left -= 1
            right += 1
            print(left, right)
        left, right = i-1, i
        print("Testing without middle letter, ", left, right)
        while left >= 0 and right < len(s) and s[left] == s[right]:
            print("new pal: ", s[left:right+1])
            if len(longest) < len(s[left:right+1]):
                longest = s[left:right+1]
                print("longest: ", longest)
            left -= 1
            right += 1
            print(left, right)
    return longest

print(longestPalindrome(palindrome))