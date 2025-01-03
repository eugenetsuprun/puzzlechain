"""Given a string consisting of digits from 2 to 9, the task is to return all possible letter combinations that correspond to the number based on a traditional telephone keypad mapping. Any non-digit characters, as well as the digits 0 and 1, should be filtered out.

The mapping is as follows:
- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Examples:

1. For the input "23", the output should be: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. For an empty input "", the output should be: [].
3. For the input "2", the output should be: ["a", "b", "c"].
4. For the input "12*30", the output should also be: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Constraints to consider:
- The length of the input string is between 0 and 4.
- Each character in the input string is a digit in the range ['2', '9'].

The function should be defined as: letterCombinations(digits: str) -> list[str]"""

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
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    backtrack(0, "")
    return combinations