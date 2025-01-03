"""Given a string that contains digits from 2 to 9, the task is to return all possible letter combinations that the digits could represent, based on the mapping similar to that of telephone buttons. 

The mapping is as follows:
- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Any non-digit characters, including ones and zeros, should be filtered out. 

Examples:

1. For the input `digits = "23"`, the output should be `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`.
2. For the input `digits = ""`, the output should be `[]`.
3. For the input `digits = "2"`, the output should be `["a", "b", "c"]`.
4. For the input `digits = "12*30"`, the output should be `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`.

Constraints:
- The length of the `digits` string can range from 0 to 4.
- Each character in `digits` must be a digit from '2' to '9'.

The function signature is: `letterCombinations(digits: str) -> list[str]`."""

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
    
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    combinations = []
    backtrack(0, "")
    return combinations