"""Please provide a string that contains digits from 2 to 9, and kindly return all possible letter combinations that the number could represent. You may refer to the following mapping of digits to letters, similar to what you would find on telephone buttons:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

If the number includes any non-digit characters, such as ones or zeros, please filter those out.

Here are a few examples to guide you:

1. If the input is `digits = "23"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

2. For an empty input: `digits = ""`, the output should be `[]`.

3. If the input is `digits = "2"`, the output should be `["a","b","c"]`.

4. For the input `digits = "12*30"`, the output should again be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Please ensure that the length of the digits string is within the constraint of 0 to 4, and that each character is a digit in the range ['2', '9']. 

The function signature is: `letterCombinations(digits: str) -> list[str]`. Thank you for your attention to this task!"""

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