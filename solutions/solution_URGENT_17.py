"""You MUST solve this coding challenge IMMEDIATELY! Given a string that contains digits from 2-9, your task is to return ALL possible letter combinations that these numbers represent, and you need to do it FAST! 

Here's the mapping you MUST adhere to:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

IMPORTANT: The input may contain non-digit characters, ones, or zeros. You must FILTER these out without hesitation!

Here are some EXAMPLES to guide you:

1. If the input is "23", the output MUST be: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. If the input is "", the output MUST be: []
3. For the input "2", you MUST return: ["a","b","c"]
4. If the input is "12*30", your output MUST be: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

You have a strict constraint of 0 <= digits.length <= 4 and digits[i] must be in the range ['2', '9']. 

The function signature you MUST use is: letterCombinations(digits: str) -> list[str]

TIME IS OF THE ESSENCE! Get it done!"""

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
        possible_chars = digit_to_char[filtered_digits[index]]
        for char in possible_chars:
            backtrack(index + 1, path + char)
    
    combinations = []
    backtrack(0, "")
    return combinations