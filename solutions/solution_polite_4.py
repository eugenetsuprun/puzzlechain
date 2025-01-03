"""Please consider the following task: you are provided with a string that contains digits ranging from 2 to 9. Your objective is to return all possible letter combinations that correspond to the digits, similar to those on a telephone keypad. You may present your results in any order you prefer.

Here is the mapping of digits to letters for your reference:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input string may include non-digit characters, as well as ones or zeros. Kindly ensure to filter these out in your implementation.

To illustrate, here are a few examples:

1. If the input is `digits = "23"`, the expected output would be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

2. If the input is `digits = ""`, the output should be an empty list: `[]`.

3. For the input `digits = "2"`, you would return `["a","b","c"]`.

4. If the input is `digits = "12*30"`, the output should again be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Please adhere to the following constraints:

- The length of the digits should be between 0 and 4 inclusive.
- Each character in the string must be a digit between '2' and '9'.

The function signature for your solution should be: `letterCombinations(digits: str) -> list[str]`."""

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