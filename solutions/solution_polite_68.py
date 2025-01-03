"""You are kindly requested to write a function that takes a string containing digits from 2 to 9 and returns all possible letter combinations that the input number could represent. Please present the answer in any order you prefer.

For your convenience, here is the mapping of digits to letters, similar to those found on telephone keypads:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input may contain some non-digit characters, as well as ones or zeros, which you should filter out.

Here are a few examples to guide you:

1. For the input `digits = "23"`, you should return `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. If the input is `digits = ""`, the output should be `[]`.
3. If the input is `digits = "2"`, the expected output is `["a","b","c"]`.
4. For the input `digits = "12*30"`, the function should return `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Please ensure that your implementation adheres to the following constraints:

- The length of `digits` should be between 0 and 4.
- Each character in `digits` must be a digit within the range ['2', '9'].

The function signature you are to use is: `letterCombinations(digits: str) -> list[str]`.

Thank you for your attention to these details!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and '1' or '0'
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