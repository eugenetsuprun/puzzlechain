"""Alright genius, listen up! You've got this string packed with digits from 2 to 9, and your mission—if you can handle it—is to whip up all the possible letter combos those numbers could stand for. You know, like how those old-school phones worked. 

Here’s the breakdown for you:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Oh, and by the way, if you spot any junk in there—like non-digits, ones, or zeros—just toss them out like yesterday's trash.

Get it? Here are your practice rounds:

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Example 4:
Input: digits = "12*30"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Oh, and keep it simple: the length of your digits should be between 0 and 4, and make sure those digits are from ['2', '9']. 

So, roll up your sleeves and get cracking with the function signature: letterCombinations(digits: str) -> list[str]. Good luck, you’ll need it!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out invalid characters
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    if not digits:
        return []
    
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