"""Given a string that includes digits from 2 to 9, your task is to return all possible letter combinations that correspond to the digits. The output should be presented in any order.

The mapping of digits to letters is as follows:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input may contain non-digit characters, as well as the digits '1' and '0'. These should be disregarded.

Examples for clarification:

1. For the input `digits = "23"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. If the input is `digits = ""`, the output should be `[]`.
3. With `digits = "2"`, the output should be `["a","b","c"]`.
4. For the input `digits = "12*30"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

The constraints are as follows:

- The length of the digits can range from 0 to 4.
- Each character in the input is a digit within the range of ['2', '9'].

The function signature is:
```python
letterCombinations(digits: str) -> list[str]
```"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and '1', '0'
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