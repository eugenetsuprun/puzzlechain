"""**URGENT**: You have an immediate task that requires your coding expertise! Given a string of digits ranging from 2-9, your mission is to return ALL possible letter combinations that this number can represent, based on the classic telephone keypad mapping. 

Here's the critical mapping you must adhere to:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

**IMPORTANT**: Ensure that you filter out any non-digit characters, including any zeros or ones that may appear in the input.

**Example Scenarios**:
1. Input: `digits = "23"` → Output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`
2. Input: `digits = ""` → Output should be `[]`
3. Input: `digits = "2"` → Output should be `["a","b","c"]`
4. Input: `digits = "12*30"` → Output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`

**Constraints**:
- The length of the input string can range from 0 to 4.
- Each character in the input string must be a digit in the range ['2', '9'].

**Function Signature Required**: `letterCombinations(digits: str) -> list[str]`

Time is of the essence! Get started on this right away!"""

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