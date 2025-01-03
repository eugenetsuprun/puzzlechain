"""Please solve the following coding challenge: Given a string comprised of digits from 2 to 9, your task is to return all possible letter combinations that these digits could represent. You may present your answer in any order.

For your reference, here is the mapping of the digits to their corresponding letters, similar to what you would find on a telephone keypad:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input may include non-digit characters, as well as the digits 0 and 1, which should be filtered out.

Here are a few examples to illustrate the task:

Example 1:
- Input: digits = "23"
- Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
- Input: digits = ""
- Output: []

Example 3:
- Input: digits = "2"
- Output: ["a","b","c"]

Example 4:
- Input: digits = "12*30"
- Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Please adhere to the following constraints:
- The length of the digits string can range from 0 to 4.
- Each character in the string is guaranteed to be a digit within the range ['2', '9'].

The function signature for your solution should be: letterCombinations(digits: str) -> list[str]. Thank you very much, and I look forward to your solution!"""

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
    
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    combinations = []
    backtrack(0, "")
    return combinations