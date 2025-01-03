"""Please provide a string that contains digits ranging from 2 to 9, and the task is to return all possible letter combinations that the number could represent. The mapping of digits to letters is as follows:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Kindly note that any non-digit characters, as well as ones or zeros, should be filtered out.

Here are a few examples to illustrate:

- For an input of `digits = "23"`, the expected output would be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
- If the input is `digits = ""`, the output should be an empty list: `[]`.
- With an input of `digits = "2"`, the output should be `["a","b","c"]`.
- Lastly, for an input of `digits = "12*30"`, the output would be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Please ensure that the length of the digits is within the constraint of 0 to 4, and that each digit is within the specified range. The function signature for your solution should be: `letterCombinations(digits: str) -> list[str]`. Thank you for your cooperation!"""

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