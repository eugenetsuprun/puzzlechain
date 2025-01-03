"""You need to act FAST! Given a string of digits from 2-9, your task is to urgently generate ALL possible letter combinations that those digits could represent, just like the classic telephone keypad! 

Here’s the critical mapping to remember:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

But beware! The input string may contain non-digit characters, including ones or zeros, which MUST be filtered out immediately!

Consider this urgent example:
- Input: digits = "23"
- Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Other cases to consider urgently:
- Input: digits = "" 
- Output: []
- Input: digits = "2"
- Output: ["a","b","c"]
- Input: digits = "12*30"
- Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Time is of the essence! You have to ensure that your solution adheres to these constraints:
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

Your function signature MUST be:
```python
def letterCombinations(digits: str) -> list[str]:
```
Now, GO, and bring those combinations to life!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
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