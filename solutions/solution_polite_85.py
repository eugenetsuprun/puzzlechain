"""Could you please develop a function that takes a string containing digits from 2 to 9 inclusive and returns all possible letter combinations that the number could represent? You may wish to consider the following mapping of digits to letters, similar to that found on telephone buttons:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that if the input string contains non-digit characters, such as ones or zeros, you should filter them out. 

Here are a few examples to illustrate the expected behavior:

1. For an input of `digits = "23"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. If the input is `digits = ""`, the output should be `[]`.
3. With an input of `digits = "2"`, the expected output is `["a","b","c"]`.
4. For `digits = "12*30"`, the output should again be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Please keep in mind the constraints that the length of the digits can range from 0 to 4, and each digit in the input must be in the range ['2', '9']. 

The function signature you should follow is: `letterCombinations(digits: str) -> list[str]`. Thank you for your assistance with this task!"""

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