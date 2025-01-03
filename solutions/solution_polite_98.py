"""Given a string that may contain digits ranging from 2 to 9, your task is to return all possible letter combinations that the number could represent. You may refer to the mapping of digits to letters, similar to those found on telephone keypads, as follows:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please be mindful that the input might include non-digit characters, as well as ones or zeros. It would be appreciated if you could filter such characters out.

For your reference, here are a few examples:
1. If the input is `digits = "23"`, the expected output would be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. In the case where the input is `digits = ""`, the output should simply be an empty list: `[]`.
3. For an input of `digits = "2"`, you should return `["a","b","c"]`.
4. If the input is `digits = "12*30"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Please adhere to the constraints that the length of `digits` can range from 0 to 4, and each character in `digits` must be a digit within the range of ['2', '9'].

The function signature for your solution should be: `letterCombinations(digits: str) -> list[str]`. Thank you for your effort in tackling this task!"""

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