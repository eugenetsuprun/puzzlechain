"""You are kindly requested to develop a function that takes a string of digits ranging from 2 to 9 and returns all possible letter combinations that the digits could represent. Please refer to the mapping of digits to letters as found on traditional telephone buttons:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Do keep in mind that the input might include non-digit characters, such as ones or zeros, which should be filtered out.

Here are a few examples to illustrate the task:

1. For the input `digits = "23"`, the expected output is `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. If the input is `digits = ""`, the output should be an empty list: `[]`.
3. With the input `digits = "2"`, the output should be `["a","b","c"]`.
4. For the input `digits = "12*30"`, the desired output is again `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Please ensure that your solution adheres to the following constraints:

- The length of `digits` should be between 0 and 4.
- Each character in `digits` must be a digit within the range ['2', '9'].

The function signature should be: `letterCombinations(digits: str) -> list[str]`. Thank you for your attention to detail and your efforts in solving this task!"""

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