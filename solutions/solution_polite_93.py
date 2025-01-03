"""Your task is to create a function that, given a string composed of digits ranging from 2 to 9, returns all possible letter combinations that these digits could represent. Please take into consideration the mapping of digits to letters as found on traditional telephone keypads:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Additionally, the string may include non-digit characters, such as ones or zeros, which should be filtered out before processing.

For your convenience, here are some examples to illustrate the expected behavior:

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

Please note the constraints for this problem:
- The length of the digits string can range from 0 to 4.
- Each character in the string must be a digit from the set ['2', '9'].

Your function should be defined with the following signature: 
```python
def letterCombinations(digits: str) -> list[str]:
```

I truly appreciate your efforts on this task and wish you the best of luck!"""

```python
def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and create a list of valid digits
    valid_digits = [d for d in digits if d in digit_to_letters]
    
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
```