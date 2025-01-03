"""Given a string composed of digits ranging from 2 to 9, it would be wonderful if you could devise a method to return all possible letter combinations that these numbers might represent. Please feel free to present the results in any order you deem fitting.

For your reference, here is a mapping of the digits to their corresponding letters, similar to how they appear on telephone keypads:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

You may encounter some non-digit characters, as well as ones and zeros within the string. Kindly filter these out as you proceed.

Here are some examples to illustrate the task:

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

As you approach this task, please keep in mind the following constraints:
- The length of the digits string will be between 0 and 4.
- Each digit in the string should be in the range of ['2', '9'].

For your implementation, you may use the following function signature:
```python
def letterCombinations(digits: str) -> list[str]:
``` 

Thank you for your attention to this task!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        digit = digits[index]
        if digit in phone_map:
            for letter in phone_map[digit]:
                backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations