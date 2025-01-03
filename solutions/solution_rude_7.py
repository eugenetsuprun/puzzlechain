"""Got a string of digits from 2 to 9? Your mission, should you choose to accept it (but seriously, just get it done), is to spit out every possible letter combo those numbers can create. You know the drill – think old-school phone buttons.

Here’s the deal:

- Button 2 = ABC
- Button 3 = DEF
- Button 4 = GHI
- Button 5 = JKL
- Button 6 = MNO
- Button 7 = PQRS
- Button 8 = TUV
- Button 9 = WXYZ

Oh, and by the way, if there are any pesky non-digit characters, ones, or zeros hanging around, just toss them out like yesterday's trash.

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

Remember, keep it to the point: 0 <= digits.length <= 4 and digits[i] is a digit from '2' to '9'. Now get to coding – or don’t, I really don’t care. 

Function signature: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
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