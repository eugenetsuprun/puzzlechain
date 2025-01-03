"""Given a string that contains digits from 2 to 9, the task is to return all possible letter combinations that the digits could represent, based on the standard telephone keypad mapping. Non-digit characters, as well as the digits '0' and '1', should be filtered out.

The mapping of digits to letters is as follows:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

For example:

- If the input is "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
- If the input is "", the output should be [].
- If the input is "2", the output should be ["a", "b", "c"].
- If the input is "12*30", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

The constraints to keep in mind are:

- The length of the digits string can range from 0 to 4.
- Each character in the digits string must be a digit from '2' to '9'.

The function signature is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_letters = digit_to_char[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    digits = ''.join(filter(lambda x: x in digit_to_char, digits))
    combinations = []
    backtrack(0, "")
    return combinations