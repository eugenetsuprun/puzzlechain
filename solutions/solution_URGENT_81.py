"""Urgent! You must solve this coding challenge immediately! Given a string containing digits from 2-9 inclusive, your task is to return **all** possible letter combinations that the number could represent. Time is of the essence—get it done fast! 

Here’s the mapping of digits to letters you need:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Be aware that the number may contain non-digit characters, including ones or zeros. Filter them out quickly!

Examples to consider:

1. Input: digits = "23"  
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: digits = ""  
   Output: []

3. Input: digits = "2"  
   Output: ["a","b","c"]

4. Input: digits = "12*30"  
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Constraints to keep in mind:

- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

Your function signature is: **letterCombinations(digits: str) -> list[str]**

**Act now!**"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
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