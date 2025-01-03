"""Your task is CRITICAL! Given a string made up of digits from 2 to 9, you MUST return all possible letter combinations that correspond to those numbers—just like the old telephone keypads! 

Here's the crucial number-to-letter mapping: 

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Don't forget to REMOVE any non-digit characters, ones, or zeros from the input! 

Consider these EXAMPLES to guide your solution:

1. Input: digits = "23"
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: digits = ""
   Output: []

3. Input: digits = "2"
   Output: ["a","b","c"]

4. Input: digits = "12*30"
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

The constraints are straightforward: 

- 0 <= digits.length <= 4 
- Each digits[i] is guaranteed to be in the range ['2', '9'].

The function signature you need to implement is: 
```python
letterCombinations(digits: str) -> list[str]
```

ACT FAST—this is a time-sensitive challenge!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and remove 0s and 1s
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