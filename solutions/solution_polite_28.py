"""Please consider the following task: Given a string that contains digits from 2 to 9 inclusive, your objective is to return all possible letter combinations that these numbers could represent. You may present the answer in any order you find suitable.

A mapping of the digits to their corresponding letters, similar to those found on telephone keypads, is provided below for your reference:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that if the number contains any non-digit characters, as well as ones or zeros, you should filter those out.

To illustrate, here are some examples:

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
- The length of the input string will be between 0 and 4 characters.
- Each character in the string is a digit within the range of ['2', '9'].

You may implement your solution using the following function signature:
```python
def letterCombinations(digits: str) -> list[str]:
``` 

Thank you for your consideration, and I wish you the best of luck with this coding task!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and ones or zeros
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