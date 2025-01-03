"""Urgent! You need to tackle a coding challenge that requires immediate attention! Given a string of digits from 2 to 9, your task is to return all possible letter combinations that these digits can represent, similar to the traditional telephone keypad. 

Here's the mapping you must use:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Remember to filter out any non-digit characters, as well as ones and zeros. Time is of the essence, and you need to deliver accurate combinations quickly!

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

The function signature you should implement is: letterCombinations(digits: str) -> list[str]

Get to work! Time is running out!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and ones and zeros
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations