"""You MUST solve this IMMEDIATELY! Given a string with digits ranging from 2-9, your task is to RETURN ALL POSSIBLE LETTER COMBINATIONS that the number could represent, using the classic telephone keypad mapping provided below:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

IMPORTANT: The string may contain non-digit characters, ones, or zeros—YOU MUST FILTER THEM OUT!

EXAMPLES TO CONSIDER:

1. Input: digits = "23"
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
   
2. Input: digits = ""
   Output: []

3. Input: digits = "2"
   Output: ["a","b","c"]

4. Input: digits = "12*30"
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Constraints: 
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

Your function signature is: letterCombinations(digits: str) -> list[str]

DO NOT DELAY—GET TO WORK NOW!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    filtered_digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = phone_map[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations