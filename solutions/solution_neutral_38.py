"""Given a string that contains digits from 2-9, the task is to return all possible letter combinations that the number could represent, based on the following mapping of digits to letters, similar to that found on telephone buttons:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Any non-digit characters, as well as the digits '1' and '0', should be filtered out.

Examples include:

1. For input "23", the output should be: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. For input "", the output should be: [].
3. For input "2", the output should be: ["a", "b", "c"].
4. For input "12*30", the output should be: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

The constraints to keep in mind are that the length of the input string can range from 0 to 4, and each character in the string should be a digit in the range ['2', '9'].

The function signature for this task is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and '1', '0'
    filtered_digits = ''.join([d for d in digits if d in digit_to_letters])
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_letters[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations