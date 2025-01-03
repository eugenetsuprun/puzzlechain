"""URGENT! You must solve this coding challenge NOW! Given a string of digits ranging from 2-9, your task is to return ALL possible letter combinations that these digits can represent, based on the classic phone keypad mapping. ACT FAST and filter out any non-digit characters, zeros, or ones from the input.

Here's the mapping you need to remember:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Consider these examples to guide you:

1. For input `"23"`, the output should be: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. An empty input `""` should yield: `[]`.
3. The input `"2"` should return: `["a","b","c"]`.
4. For input `"12*30"`, ensure you get: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Remember, the constraints are simple: 0 <= digits.length <= 4 and only digits in the range ['2', '9'] are valid.

Your function signature must be: `letterCombinations(digits: str) -> list[str]`

Get to it IMMEDIATELY! Time is of the essence!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and invalid digits
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