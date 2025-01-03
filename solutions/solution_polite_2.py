"""Please create a function that takes a string of digits ranging from 2 to 9 and returns all possible letter combinations that these digits could represent. The mapping of digits to letters, similar to that found on traditional telephone buttons, is as follows:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

It is important to note that the input string may contain non-digit characters, as well as ones and zeros, which should be filtered out.

Here are a few examples to illustrate the expected input and output:

1. For the input `digits = "23"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. If `digits = ""`, the output should be `[]`.
3. With `digits = "2"`, the output should be `["a","b","c"]`.
4. In the case of `digits = "12*30"`, the output should again be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

For your implementation, please make sure the function adheres to the following constraints:

- The length of the digits should be between 0 and 4.
- Each character in the input string should be a digit in the range of ['2', '9'].

The function signature should be as follows: `letterCombinations(digits: str) -> list[str]`. Thank you for your attention to detail in this task!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
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