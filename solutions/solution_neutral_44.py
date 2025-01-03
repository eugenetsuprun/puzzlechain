"""Given a string that contains the digits from 2 to 9, your task is to return all possible letter combinations that the digits could represent, based on the classic telephone keypad mapping. The mapping is as follows:

- 2 corresponds to ABC
- 3 corresponds to DEF
- 4 corresponds to GHI
- 5 corresponds to JKL
- 6 corresponds to MNO
- 7 corresponds to PQRS
- 8 corresponds to TUV
- 9 corresponds to WXYZ

Please note that the input string may include non-digit characters, as well as the digits 0 or 1, which should be filtered out.

Examples:

1. For the input "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. For the input "", the output should be [].
3. For the input "2", the output should be ["a", "b", "c"].
4. For the input "12*30", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Constraints to consider:

- The length of the input string can range from 0 to 4.
- Each character in the string should be a digit in the range from '2' to '9'.

The function signature for your implementation should be: letterCombinations(digits: str) -> list[str]."""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and digits 0 and 1
    filtered_digits = ''.join([d for d in digits if d in phone_map])
    
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