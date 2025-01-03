"""You are invited to tackle an engaging coding challenge. The task is to develop a function that takes a string comprised of digits ranging from 2 to 9 and returns all possible letter combinations corresponding to those digits. This mapping mirrors the typical layout of letters on telephone keypads, as outlined below:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input string may include non-digit characters, as well as the digits one or zero. Your task will be to filter these out and focus solely on the relevant digits.

Here are a few examples to illustrate the expected functionality:

1. If the input is `digits = "23"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. For an empty input, `digits = ""`, the output should simply be `[]`.
3. With `digits = "2"`, you should return `["a","b","c"]`.
4. If the input is `digits = "12*30"`, the expected output is `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Please be mindful of the following constraints:
- The length of the input string will be between 0 and 4.
- Each character in `digits` will be a digit within the range of ['2', '9'].

The signature for your function should be: `letterCombinations(digits: str) -> list[str]`.

Thank you for your thoughtful consideration, and I wish you the best of luck with this task!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    filtered_digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = phone_map[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations