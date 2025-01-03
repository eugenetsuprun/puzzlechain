"""Given a string that contains digits between 2 and 9, the task is to generate all possible letter combinations corresponding to those digits based on the mapping typically found on telephone keypads. The mapping is as follows:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Any non-digit characters, as well as the digits 0 and 1, should be disregarded in the processing of the input.

Examples to consider:

1. If the input is "23", the output should be ["ad","ae","af","bd","be","bf","cd","ce","cf"].
2. If the input is an empty string, the output should be [].
3. If the input is "2", the output should be ["a","b","c"].
4. If the input is "12*30", the output should again be ["ad","ae","af","bd","be","bf","cd","ce","cf"].

Keep in mind the following constraints:

- The length of the input string is between 0 and 4.
- Each character in the input string must be a digit in the range from '2' to '9'.

The function signature for implementing this solution is: letterCombinations(digits: str) -> list[str]."""

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