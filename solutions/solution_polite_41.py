"""Given a string composed of digits ranging from 2 to 9, your task is to return all possible letter combinations that the number could represent. You may present the answer in any order that you find convenient.

Below is the mapping of digits to letters, similar to what you would find on telephone keypads:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input number may contain some non-digit characters, as well as ones or zeros. We would appreciate it if you could filter those out.

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

For your convenience, here are the constraints to keep in mind:
- The length of the digits string is between 0 and 4.
- Each character in the string is a digit from the range ['2', '9'].

The function signature you should use is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and '1' or '0'
    filtered_digits = ''.join(filter(lambda x: x in digit_to_letters, digits))
    
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