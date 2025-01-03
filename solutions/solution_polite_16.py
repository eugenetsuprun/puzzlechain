"""You are kindly requested to solve a coding task that involves generating all possible letter combinations from a given string of digits ranging from 2 to 9. To assist in your task, please refer to the following mapping of digits to letters, which resembles the layout of telephone keypads:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input string may include non-digit characters, zeros, or ones, which you should filter out. 

Here are a few examples for your reference:

1. For the input `digits = "23"`, the expected output is `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. If the input is an empty string, `digits = ""`, the expected output should be `[]`.
3. For the input `digits = "2"`, the anticipated output is `["a","b","c"]`.
4. Lastly, if the input is `digits = "12*30"`, the output should again be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Please ensure that your solution adheres to the following constraints: the length of `digits` must be between 0 and 4, and each character in `digits` must be a digit within the range of ['2', '9'].

The function you will implement should be defined as: 
```python
def letterCombinations(digits: str) -> list[str]:
```

Thank you for your attention to this task!"""

```python
def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
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
```