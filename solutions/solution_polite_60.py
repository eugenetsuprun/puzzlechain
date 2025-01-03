"""You are invited to solve a coding task that involves generating all possible letter combinations from a given string of digits, specifically those ranging from 2 to 9. This task involves a mapping akin to that found on telephone keypads, where each digit corresponds to a set of letters:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input string may contain non-digit characters, including ones or zeros, which should be filtered out. 

For your reference, here are a few examples to illustrate the expected input and output:

1. If the input is `digits = "23"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. For an empty input, `digits = ""`, the output should be `[]`.
3. For a single digit, `digits = "2"`, the output should be `["a","b","c"]`.
4. If the input includes non-digit characters, such as `digits = "12*30"`, the output should still be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Please ensure that your solution adheres to the following constraints:
- The length of the input string will be between 0 and 4.
- Each character in the input string will be a digit within the range ['2', '9'].

The function signature you will implement is: `letterCombinations(digits: str) -> list[str]`. Thank you for your attention to detail in this task!"""

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