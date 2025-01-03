"""Given a string that contains digits from 2 to 9, your task is to return all possible letter combinations that these digits could represent, based on the following mapping similar to telephone buttons:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Make sure to filter out any non-digit characters, as well as the digits 0 and 1, from the input.

Examples to consider:

1. For the input `digits = "23"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. For the input `digits = ""`, the output should be `[]`.
3. For the input `digits = "2"`, the output should be `["a","b","c"]`.
4. For the input `digits = "12*30"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Constraints to keep in mind include:
- The length of the digits string will be between 0 and 4.
- Each character in the string will be a digit between '2' and '9'.

The function signature for this task is: `letterCombinations(digits: str) -> list[str]`."""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and digits 0 and 1
    filtered_digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    if not filtered_digits:
        return []
    
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