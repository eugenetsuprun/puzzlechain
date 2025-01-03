"""Urgent! You need to solve the following coding task immediately. Given a string containing digits from 2-9, your mission is to return all possible letter combinations that the number could represent—time is critical! Remember, you must filter out any non-digit characters, including ones and zeros. 

Refer to the mapping below for how each digit corresponds to letters:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

You have to handle various input scenarios including:
1. Input: "23" should yield Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
2. Input: "" should yield Output: []
3. Input: "2" should yield Output: ["a", "b", "c"]
4. Input: "12*30" should yield Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Your code needs to conform to the constraints:
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

The function signature is: `letterCombinations(digits: str) -> list[str]`. Get to it NOW!"""

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