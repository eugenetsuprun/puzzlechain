"""Given a string consisting of digits between 2 and 9, the task is to generate all possible letter combinations that these digits could represent, similar to the mapping found on telephone keypads.

The mapping is as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Any non-digit characters, as well as the digits 0 and 1, should be ignored.

Example cases include:

1. For input `digits = "23"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. For input `digits = ""`, the output should be `[]`.
3. For input `digits = "2"`, the output should be `["a","b","c"]`.
4. For input `digits = "12*30"`, the output should also be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

The constraints are that the length of the `digits` string can range from 0 to 4 and each character in `digits` will be restricted to the digits '2' through '9'.

The function signature should be: `letterCombinations(digits: str) -> list[str]`."""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations