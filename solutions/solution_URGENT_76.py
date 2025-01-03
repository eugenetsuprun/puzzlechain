"""**URGENT: You are faced with a critical coding challenge!** Given a string of digits (ranging from 2-9), your task is to return ALL possible letter combinations that these digits could represent. Time is of the essence! 

Refer to the mapping below for the letters associated with each digit:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Remember, the input string may contain non-digit characters, ones, or zeros. You MUST filter these out before processing!

**Examples to guide you:**

1. Input: `digits = "23"`  →  Output: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`
2. Input: `digits = ""`  →  Output: `[]`
3. Input: `digits = "2"`  →  Output: `["a","b","c"]`
4. Input: `digits = "12*30"`  →  Output: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`

**Constraints:**
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

The function signature you need to implement is: `letterCombinations(digits: str) -> list[str]`. 

**Get to work NOW and solve this problem with urgency!**"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and ones/zeros
    filtered_digits = ''.join(filter(lambda x: x in digit_to_letters, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_letters[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations