"""**URGENT: Coding Challenge!**

You need to tackle a coding task that demands immediate attention! Given a string of digits from 2-9, your mission is to return **all possible letter combinations** that these numbers represent, similar to the letters on a telephone keypad. Be aware that the input may include non-digit characters, as well as ones or zeros—your job is to **filter those out**!

Here's the critical mapping you need to remember:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

**Key Examples to Guide You:**

1. Input: digits = "23" 
   - Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: digits = "" 
   - Output: []

3. Input: digits = "2" 
   - Output: ["a","b","c"]

4. Input: digits = "12*30" 
   - Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

**Constraints You Must Follow:**

- The length of the digits is between 0 and 4.
- Each digit must be in the range of ['2', '9'].

**Function Signature:**
```python
def letterCombinations(digits: str) -> list[str]:
```

Time is of the essence! Get to coding and solve this challenge NOW!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
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