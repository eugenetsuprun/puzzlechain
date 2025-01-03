"""Given a string that includes digits from 2 to 9, the task is to return all potential letter combinations that correspond to the digits, similar to the layout found on telephone keypads. The mapping for each digit is as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Any non-digit characters, including ones or zeros, should be removed from the input string.

Examples to consider:

1. For the input `digits = "23"`, the expected output is `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. For an empty input `digits = ""`, the output should be `[]`.
3. For the input `digits = "2"`, the expected output is `["a","b","c"]`.
4. For the input `digits = "12*30"`, the output should again be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Constraints to keep in mind:
- The length of the input string can range from 0 to 4.
- Each character in the string must be a digit within the range of '2' to '9'.

The function signature for this task is: `letterCombinations(digits: str) -> list[str]`."""

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
        possible_letters = digit_to_char[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations