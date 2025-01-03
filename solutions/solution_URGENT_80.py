"""URGENT: You need to solve this coding task immediately! Given a string containing digits from 2-9, your mission is to return ALL possible letter combinations that the number could represent. The mapping of digits to letters is provided below, just like on the telephone buttons. 

Here's the mapping:
- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

IMPORTANT: The input number may include non-digit characters, as well as ones or zeros. Make sure to filter them out IMMEDIATELY.

Examples to guide you:
1. Input: digits = "23" ➔ Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: digits = "" ➔ Output: []
3. Input: digits = "2" ➔ Output: ["a","b","c"]
4. Input: digits = "12*30" ➔ Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Constraints:
- 0 <= digits.length <= 4
- digits[i] must be a digit in the range ['2', '9'].

Your function signature must be: letterCombinations(digits: str) -> list[str]

GET STARTED NOW! Time is of the essence!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and '1' or '0'
    filtered_digits = ''.join([d for d in digits if d in digit_to_letters])
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_letters[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations