"""Please devise a function that takes a string composed of digits ranging from 2 to 9 and returns all the potential letter combinations corresponding to those digits, much like the mappings found on telephone keypads. 

Here is the mapping for your reference:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Do keep in mind that the input string may include non-digit characters, as well as the digits zero and one, which should be filtered out before processing.

To illustrate, here are a few examples:

1. For the input `digits = "23"`, the expected output is `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. If the input is `digits = ""`, the output should simply be `[]`.
3. For `digits = "2"`, you would return `["a","b","c"]`.
4. If the input is `digits = "12*30"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Please bear in mind the constraints: the length of the input string can vary from 0 to 4, and each character in the string must be a digit within the range of '2' to '9'.

The function signature is as follows: `letterCombinations(digits: str) -> list[str]`. Thank you for your attention to this task!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and digits 0 and 1
    filtered_digits = ''.join([d for d in digits if d in digit_to_char])
    
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