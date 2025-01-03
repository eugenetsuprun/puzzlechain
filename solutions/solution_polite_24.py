"""Please find below a coding task that requires your attention. You are invited to develop a function that, given a string containing digits from 2 to 9 inclusive, returns all possible letter combinations that the number could represent. The output can be provided in any order.

To assist you further, here is the mapping of digits to letters, akin to the layout on telephone buttons:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input string may contain non-digit characters, including ones or zeros, and your task will be to filter those out.

Here are a few examples to elucidate the requirements:

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
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

The function signature you should follow is: 
```python
letterCombinations(digits: str) -> list[str]
```

Thank you for your attention to this task, and I look forward to your insightful solution!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
    valid_digits = ''.join(filter(lambda x: x in digit_to_letters, digits))
    
    if not valid_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(valid_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_letters[valid_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations