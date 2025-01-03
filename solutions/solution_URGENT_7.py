"""URGENT: You must tackle this coding task IMMEDIATELY! Given a string of digits from 2-9, your mission is to return ALL possible letter combinations these numbers can create, using the classic telephone keypad mapping! 

Here’s the mapping you need to remember:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

*IMPORTANT*: The input string may contain non-digit characters, as well as ones or zeros. You MUST filter out any invalid characters!

Examples you MUST consider:

1. Input: digits = "23"
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: digits = ""
   Output: []

3. Input: digits = "2"
   Output: ["a","b","c"]

4. Input: digits = "12*30"
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

**Constraints to keep in mind**:
- The length of the digits string is between 0 and 4.
- Each digit must be in the range ['2', '9'].

Get to work on the function signature: `letterCombinations(digits: str) -> list[str]`. Time is of the essence! Do NOT delay!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out invalid characters
    valid_digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    if not valid_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(valid_digits):
            combinations.append(path)
            return
        possible_letters = phone_map[valid_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations