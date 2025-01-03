"""You are kindly requested to develop a solution for a coding task that involves generating all possible letter combinations based on a given string of digits ranging from 2 to 9. Each digit corresponds to specific letters, similar to those found on a telephone keypad. 

The mapping for the digits is as follows:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input string may include non-digit characters, as well as the digits one and zero, which should be filtered out appropriately.

Here are a few examples to illustrate the expected input and output:

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

Please ensure that your solution adheres to the constraints provided, which specify that the length of the digits string can range from 0 to 4, and that each character in the string must be a digit within the range of '2' to '9'.

The function signature for your implementation should be as follows: 
```python
def letterCombinations(digits: str) -> list[str]:
``` 

Your attention to detail and adherence to the requirements of this task are greatly appreciated. Thank you for your efforts!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    filtered_digits = [d for d in digits if d in digit_to_letters]
    
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