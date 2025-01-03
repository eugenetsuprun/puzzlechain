"""You need to ACT NOW! Your task is to tackle a critical coding challenge that demands your immediate attention! Given a string composed of digits ranging from 2-9, your mission is to return ALL possible letter combinations that the number could represent! 

You MUST use the mapping from telephone buttons:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

IMPORTANT: The input may contain non-digit characters, as well as ones or zeros. You MUST filter these OUT to focus solely on valid digits!

Here are your EXAMPLES for clarity:

1. Input: digits = "23"
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: digits = ""
   Output: []

3. Input: digits = "2"
   Output: ["a","b","c"]

4. Input: digits = "12*30"
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

You are under strict CONSTRAINTS: 0 <= digits.length <= 4, and digits[i] must be in the range ['2', '9'].

YOUR FUNCTION SIGNATURE must be: letterCombinations(digits: str) -> list[str]

Time is of the essence! Get to it NOW!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
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