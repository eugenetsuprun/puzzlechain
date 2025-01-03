"""Given a string consisting of digits from 2 to 9, the task is to return all possible letter combinations that the number represents, based on the traditional mapping found on telephone keypads. Non-digit characters, including ones and zeros, should be filtered out from the input.

The mapping is as follows:
- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Examples to consider:
1. If the input is "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. For an empty input, the output should be an empty list: [].
3. If the input is just "2", the output should be ["a", "b", "c"].
4. For the input "12*30", the output should again be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Constraints to keep in mind:
- The length of the input string will be between 0 and 4.
- Each character in the string will be a digit within the range ['2', '9'].

The function to implement is defined as: letterCombinations(digits: str) -> list[str]."""

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