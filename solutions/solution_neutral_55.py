"""Given a string that contains digits from 2 to 9 inclusive, the task is to return all possible letter combinations that correspond to the digits, similar to how letters are mapped on telephone buttons. Non-digit characters, as well as any instances of digits '1' or '0', should be ignored in the input.

The digit-to-letter mapping is as follows:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

For example:
- Input: "23" should yield an output of ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
- Input: "" should yield an output of [].
- Input: "2" should yield an output of ["a", "b", "c"].
- Input: "12*30" should yield an output of ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

The expected function signature is: `letterCombinations(digits: str) -> list[str]`. 

Constraints for the input are as follows:
- The length of `digits` can be between 0 and 4.
- Each character in `digits` must be a digit in the range ['2', '9']."""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_letters = digit_to_letters[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    digits = ''.join(filter(lambda x: x in digit_to_letters, digits))
    backtrack(0, "")
    return combinations