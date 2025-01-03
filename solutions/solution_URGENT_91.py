"""URGENT: You are tasked with solving a critical coding challenge. You need to take a string that may contain digits from 2 to 9, and you must return ALL possible letter combinations that these digits can represent, just like you would find on a telephone keypad! 

Here’s the mapping you must work with:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

IMPORTANT: The input may contain non-digit characters, zeros, or ones. You MUST filter these out before processing. 

EXAMPLES to guide your implementation:
1. Input: digits = "23" should yield Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: digits = "" must yield Output: []
3. Input: digits = "2" must yield Output: ["a","b","c"]
4. Input: digits = "12*30" must yield Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Be aware of the constraints: 
- 0 <= digits.length <= 4
- Each digit in digits is guaranteed to be in the range ['2', '9'].

Your function signature should be: letterCombinations(digits: str) -> list[str]

Time is of the essence! Get this solved NOW!"""

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