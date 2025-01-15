# Given two positive integers num1 and num2, find the positive integer x such that:

# x has the same number of set bits as num2, and
# The value x XOR num1 is minimal.
# Note that XOR is the bitwise XOR operation.

# Return the integer x. The test cases are generated such that x is uniquely determined.

# The number of set bits of an integer is the number of 1's in its binary representation.

 

# Example 1:

# Input: num1 = 3, num2 = 5
# Output: 3
# Explanation:
# The binary representations of num1 and num2 are 0011 and 0101, respectively.
# The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.


# Example 2:

# Input: num1 = 1, num2 = 12
# Output: 3
# Explanation:
# The binary representations of num1 and num2 are 0001 and 1100, respectively.
# The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.
 

# Constraints:

# 1 <= num1, num2 <= 109

def minimizeXor(num1: int, num2: int) -> int:
    def numSetBits(bits: str):
        num = 0
        for i in range(len(bits)):
            if bits[i] == '1': 
                num += 1
        print("num set bits: ", bits, num)
        return num
    
    def getBitValue(num: int):
        print("get bits: ", num)
        maxMod = 1
        while maxMod*2 <= num:
            maxMod = maxMod*2
        print(maxMod)
        bits = ''
        while maxMod >= 1:
            if num - maxMod >= 0:
                num -= maxMod
                maxMod = maxMod / 2
                bits = bits + '1'
            else:
                maxMod = maxMod / 2
                bits = bits + '0'
        print(bits)
        return bits
    
    def getIntValue(bits: str):
        expmod = 2 ** (len(bits)-1) 
        num = 0
        for i in range(len(bits)):
            num += int(bits[i]) * expmod
            expmod = expmod // 2
        print("get int: ", bits, num)
        return num
    
    minValue = ''
    numBitsNeeded = numSetBits(getBitValue(num2))
    xornum = getBitValue(num1)
    print(xornum, numBitsNeeded)
    for i in range(len(xornum)):
        if numBitsNeeded > 0:
            if xornum[i] == '1':
                numBitsNeeded -= 1
                minValue += '1'
            else:
                minValue += '0'
        else:
            minValue += '0'


    i = len(minValue) - 1
    while numBitsNeeded > 0 and i >= 0:
        print("add more ones")
        print(minValue)
        if minValue[i] == '0':
            print(minValue[:i], minValue[i+1:])
            minValue = minValue[:i] + '1' + minValue[i+1:]
            numBitsNeeded -= 1
        i -= 1
    while numBitsNeeded > 0:
        print("MORE ONES")
        minValue = '1' + minValue
        numBitsNeeded -= 1

    return getIntValue(minValue)

print(minimizeXor(73, 32))
# print(minimizeXor(5, 9))