"""Alright, listen up! You’ve got this string of digits between 2 and 9, and your job is to whip up all the possible letter combos those numbers can crank out. Just like the buttons on a phone, capisce? 

Here’s the deal: 

- 2 maps to ABC
- 3 maps to DEF
- 4 maps to GHI
- 5 maps to JKL
- 6 maps to MNO
- 7 maps to PQRS
- 8 maps to TUV
- 9 maps to WXYZ

Oh, and if you see any junk like non-digit characters, or zeros and ones, just toss 'em out. We don't need that nonsense!

Check these examples to get your brain moving:

1. Input: digits = "23" 
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: digits = "" 
   Output: []

3. Input: digits = "2" 
   Output: ["a","b","c"]

4. Input: digits = "12*30" 
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Now, don’t screw this up! The function signature is: letterCombinations(digits: str) -> list[str] 
Get to it!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        current_digit = digits[index]
        if current_digit in digit_to_char:
            for char in digit_to_char[current_digit]:
                backtrack(index + 1, path + char)
    
    combinations = []
    digits = ''.join(filter(str.isdigit, digits))  # Filter out non-digit characters
    backtrack(0, "")
    return combinations