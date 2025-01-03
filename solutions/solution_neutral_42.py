"""Given a string composed of digits from 2 to 9, the task is to return all potential letter combinations that the number can represent. The response can be presented in any order.

The mapping of digits to letters, as found on telephone keypads, is as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Note that the input may include non-digit characters, ones, or zeros, which should be disregarded.

Examples for clarity:

1. If the input is "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. For an empty input, the output should be [].
3. For an input of "2", the output should be ["a", "b", "c"].
4. If the input is "12*30", the output should match the valid combinations from "23", resulting in ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Constraints to consider:
- The length of the input string ranges from 0 to 4.
- Each character in the input string is a digit falling within the range of '2' to '9'.

The function signature is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and ones/zeros
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