"""Given a string comprised of digits ranging from 2 to 9, the task is to return all potential letter combinations that correspond to the input number. The results can be presented in any order.

The mapping of each digit to its associated letters is as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

It is important to note that the input may contain non-digit characters, as well as the digits 0 and 1, which should be filtered out.

Example inputs and their expected outputs are:

1. For the input "23", the output should include combinations such as ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. For an empty input "", the output should be [].
3. For the input "2", the output should be ["a", "b", "c"].
4. For the input "12*30", the output should consist of combinations like ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Constraints to keep in mind:
- The length of the input string can range from 0 to 4.
- Each character in the string must be a digit within the range ['2', '9'].

The function signature for this task is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and digits 0 and 1
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