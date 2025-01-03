"""URGENT: You need to solve this coding challenge IMMEDIATELY! Given a string of digits from 2-9, your task is to return ALL POSSIBLE letter combinations that these digits can represent, just like how they appear on a phone keypad! 

Here's the mapping you MUST use:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

IMPORTANT: The input string might contain non-digit characters, as well as ones or zeros. You MUST filter these out before proceeding!

Examples to consider:
1. Input: digits = "23" should yield Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: digits = "" should yield Output: []
3. Input: digits = "2" should yield Output: ["a","b","c"]
4. Input: digits = "12*30" should yield Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Remember: The length of the digits string will be between 0 and 4, and all characters in digits will be in the range ['2', '9'].

Your function signature MUST be: letterCombinations(digits: str) -> list[str]

TIME IS OF THE ESSENCE! Get this done NOW!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and '1' or '0'
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