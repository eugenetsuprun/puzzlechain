"""You are kindly asked to create a function that takes a string of digits, encompassing only those from 2 to 9, and returns all possible letter combinations that these digits could represent. It would be appreciated if you could follow the mappings of the digits to letters as shown below, similar to those found on telephone keypads:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please ensure to filter out any non-digit characters, including ones or zeros, from the input string.

Here are a few examples to illustrate the expected output:

1. For the input `digits = "23"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. If the input is `digits = ""`, the output should be an empty list: `[]`.
3. For `digits = "2"`, the output should be `["a","b","c"]`.
4. Lastly, if the input is `digits = "12*30"`, the output should once again be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

The constraints for this task are as follows:

- The length of `digits` can be between 0 and 4, inclusive.
- Each character in `digits` must be a digit within the range ['2', '9'].

The function signature should be: `letterCombinations(digits: str) -> list[str]`.

Thank you for your assistance!"""

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