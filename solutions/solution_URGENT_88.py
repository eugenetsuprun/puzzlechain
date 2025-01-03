"""**URGENT CODING CHALLENGE!**

You are tasked with a critical coding assignment: Given a string containing digits from 2-9 inclusive, your mission is to return ALL possible letter combinations that the number could represent! Time is of the essence, and you must present the answer in ANY ORDER.

Refer to the mapping below to decode the digits into letters (just like the classic telephone buttons):

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

**IMPORTANT:** The input number may contain non-digit characters, as well as ones or zeros. You MUST filter those out before processing!

**Examples to guide your implementation:**

1. Input: digits = "23"  
   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

2. Input: digits = ""  
   Output: []

3. Input: digits = "2"  
   Output: ["a", "b", "c"]

4. Input: digits = "12*30"  
   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

**Constraints:**  
- The length of digits is between 0 and 4.  
- Each digit in digits is guaranteed to be within the range ['2', '9'].

You must implement the function with the signature: `letterCombinations(digits: str) -> list[str]`

Hurry, the clock is ticking! Get started now!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    filtered_digits = ''.join(filter(lambda x: x in digit_to_char, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_char[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations