"""**URGENT: Immediate Action Required!**

You have a critical task at hand that demands your coding expertise! You must swiftly develop a function that processes a given string of digits (ranging from 2-9) and returns all possible letter combinations represented by those digits. The time is of the essence!

**Mapping of Digits to Letters:**
- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

**Important Note:** Any non-digit characters, including ones and zeros, must be filtered out immediately!

**Example Inputs and Outputs for Quick Reference:**
1. Input: `digits = "23"` → Output: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`
2. Input: `digits = ""` → Output: `[]`
3. Input: `digits = "2"` → Output: `["a","b","c"]`
4. Input: `digits = "12*30"` → Output: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`

**Constraints to Keep in Mind:**
- 0 <= digits.length <= 4
- Each digits[i] must be a digit in the range ['2', '9'].

**Function Signature Required:**
```python
def letterCombinations(digits: str) -> list[str]:
```

Act swiftly and ensure your solution is flawless! The clock is ticking!"""

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