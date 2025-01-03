"""You are kindly requested to devise a function that takes a string comprised of digits ranging from 2 to 9, inclusive, and returns all possible letter combinations that the number could represent. You may present the results in any order you find suitable.

For your reference, below is the mapping of digits to letters, akin to those on telephone keypads:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please be mindful that the input may include non-digit characters, as well as the digits one and zero. You are encouraged to filter out any such characters.

Here are a few examples to guide you:

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

Please note the following constraints for your implementation:
- The length of digits will range from 0 to 4.
- Each character in digits is guaranteed to be a digit in the range ['2', '9'].

The function you are to create should utilize the following signature:
```python
def letterCombinations(digits: str) -> list[str]:
``` 

Thank you for your attention to this task!"""

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