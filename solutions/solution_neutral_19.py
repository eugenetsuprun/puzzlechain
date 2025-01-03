"""Given a string of digits ranging from 2 to 9, your task is to generate all possible letter combinations that the digits can represent, similar to the letter mapping found on telephone keypads. 

Here's the letter mapping for reference:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input string may contain non-digit characters, as well as ones or zeros, which should be disregarded during the process.

Consider the following examples:

1. For the input `digits = "23"`, the expected output is `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. If the input is `digits = ""`, the output should be `[]`.
3. An input of `digits = "2"` should yield `["a","b","c"]`.
4. For the input `digits = "12*30"`, the output would again be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Keep in mind the constraints:
- The length of `digits` can range from 0 to 4.
- Each character in `digits` must be between '2' and '9'.

The function signature you should implement is: `letterCombinations(digits: str) -> list[str]`."""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_letters[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    filtered_digits = [d for d in digits if d in digit_to_letters]
    combinations = []
    backtrack(0, "")
    return combinations