"""Given a string that contains digits from 2 to 9, the task is to return all possible letter combinations corresponding to the digits, similar to the mapping found on telephone buttons. The digits may include non-digit characters, ones, or zeros, which should be filtered out.

The digit-to-letter mapping is as follows:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Examples to consider:

1. For an input of digits = "23", the expected output is ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. For an input of digits = "", the expected output is [].
3. For an input of digits = "2", the expected output is ["a", "b", "c"].
4. For an input of digits = "12*30", the expected output is ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Constraints to keep in mind:

- The length of the digits string will be between 0 and 4.
- Each character in the input string is guaranteed to be a digit from '2' to '9'.

The function signature is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    # Filter out non-digit characters and ones or zeros
    filtered_digits = ''.join(filter(lambda x: x in digit_to_letters, digits))
    
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