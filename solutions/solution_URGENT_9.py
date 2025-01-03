"""You must solve a critical coding challenge immediately! Given a string consisting of digits from 2-9, your task is to generate ALL possible letter combinations that correspond to the number, based on the traditional phone keypad mapping. 

Here's the urgent mapping you need to follow:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

IMPORTANT: The input may contain non-digit characters, including 0s and 1s. You MUST filter these out before processing.

You MUST return the combinations in any order. 

Here are some examples to guide your solution:

- Input: digits = "23"
  - Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

- Input: digits = ""
  - Output: []

- Input: digits = "2"
  - Output: ["a","b","c"]

- Input: digits = "12*30"
  - Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Remember the constraints:
- The length of digits must be between 0 and 4.
- Each digit must be within the range ['2', '9'].

The function you need to implement is: 
```python
def letterCombinations(digits: str) -> list[str]:
```

Time is of the essence! Get to coding and produce the required outputs immediately!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
    filtered_digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = phone_map[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations