"""**URGENT: Solve This Coding Challenge Now!**

You are tasked with a critical coding problem that requires immediate attention! Given a string that may contain digits from 2 to 9, you must return ALL possible letter combinations that these numbers could represent, using the classic telephone keypad mapping. Be aware: the input may include non-digit characters, as well as ones and zeros, so make sure to filter them OUT!

**Mapping of digits to letters:**
- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

**Examples to illustrate the task:**
1. Input: `digits = "23"`  |  Output: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`
2. Input: `digits = ""`  |  Output: `[]`
3. Input: `digits = "2"`  |  Output: `["a","b","c"]`
4. Input: `digits = "12*30"`  |  Output: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`

**Constraints:**
- The length of `digits` can range from 0 to 4.
- Ensure `digits[i]` falls within the range ['2', '9'].

You need to implement the function signature: `letterCombinations(digits: str) -> list[str]`

Get to work NOW and solve this challenge with urgency! Time is of the essence!"""

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