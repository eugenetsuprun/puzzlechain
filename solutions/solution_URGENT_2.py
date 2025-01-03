"""You need to tackle a critical coding challenge RIGHT NOW! The task is to extract all possible letter combinations from a string of digits (2-9), based on the classic telephone keypad mappings. Here’s the urgency: 

- **Input:** A string of digits which may also include non-digit characters (like ones and zeros), which you MUST filter out.
- **Output:** An array of all possible letter combinations in ANY order!

**Key Mappings:**
- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

**Example Scenarios:**
1. For input `"23"`, you must output combinations like `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. For an empty input `""`, the output should simply be `[]`.
3. An input like `"2"` should yield `["a","b","c"]`.
4. Filter out inputs like `"12*30"` and return the valid results such as `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

You have to implement this NOW! The function signature you’ll use is: `letterCombinations(digits: str) -> list[str]`. Don’t waste another second—get coding!"""

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