"""Given a string comprised of digits ranging from 2 to 9, the task is to return all possible letter combinations that the digits could represent, in any order. Each digit corresponds to letters as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Any non-digit characters, as well as the digits '0' and '1', should be disregarded from the input.

Examples to illustrate the expected output:

1. For input `digits = "23"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. For input `digits = ""`, the output should return an empty list `[]`.
3. For input `digits = "2"`, the output should be `["a","b","c"]`.
4. For input `digits = "12*30"`, the output should yield `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

The function signature for this task is: `letterCombinations(digits: str) -> list[str]`. 

Constraints to consider:
- The length of `digits` can range from 0 to 4.
- Each `digits[i]` is guaranteed to be a digit within the range ['2', '9']."""

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