"""URGENT: You need to solve this coding challenge IMMEDIATELY! Given a string that contains digits from 2 to 9, your task is to return ALL possible letter combinations that the number could represent based on the classic telephone keypad mapping. 

Here’s the mapping you MUST use:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

FILTER out any non-digit characters (including 0s and 1s) from the input string. 

Examples to guide you:
1. Input: digits = "23" → Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: digits = "" → Output: []
3. Input: digits = "2" → Output: ["a","b","c"]
4. Input: digits = "12*30" → Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Remember the constraints:
- The length of digits is between 0 and 4.
- Each character in digits must be in the range ['2', '9'].

The function signature is: letterCombinations(digits: str) -> list[str]

TIME IS OF THE ESSENCE! Get started on this IMMEDIATELY!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only 2-9
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