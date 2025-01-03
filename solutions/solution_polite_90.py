"""You are kindly requested to develop a function that, given a string containing digits from 2 to 9 inclusive, will return all possible letter combinations corresponding to those digits. The combinations should be returned in any order that you prefer.

For your reference, here is the mapping of digits to letters, resembling the configuration found on telephone keypads:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input string may contain non-digit characters, as well as ones or zeros, which you should simply filter out.

To illustrate, here are a few examples:

1. For an input of `digits = "23"`, the expected output would be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. If the input is an empty string, `digits = ""`, the output should be `[]`.
3. For `digits = "2"`, the output should be `["a","b","c"]`.
4. In the case of `digits = "12*30"`, you would provide the output `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Please ensure your solution adheres to the following constraints:

- The length of `digits` must be between 0 and 4, inclusive.
- Each character in `digits` should be a digit in the range ['2', '9'].

The signature for your function should be: `letterCombinations(digits: str) -> list[str]`. Thank you for your attention to this task!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    filtered_digits = [d for d in digits if d in digit_to_letters]
    
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