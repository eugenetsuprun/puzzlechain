"""Given a string that contains digits ranging from 2 to 9, your task is to return all possible letter combinations that the number could represent. Please note that the output can be in any order.

For your reference, here is the mapping of digits to their corresponding letters, similar to the layout on telephone keypads:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please ensure to filter out any non-digit characters, as well as any instances of the digits one or zero.

Here are a few examples to illustrate the expected output:

Example 1:
- Input: digits = "23"
- Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Example 2:
- Input: digits = ""
- Output: []

Example 3:
- Input: digits = "2"
- Output: ["a", "b", "c"]

Example 4:
- Input: digits = "12*30"
- Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Please keep in mind the following constraints:
- The length of the digits string will be between 0 and 4, inclusive.
- Each character in the digits string will be a digit in the range ['2', '9'].

The function signature you should use is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    backtrack(0, "")
    return combinations