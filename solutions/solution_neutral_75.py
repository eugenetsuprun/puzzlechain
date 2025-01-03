"""Given a string consisting of digits between 2 and 9, your task is to determine all possible letter combinations that the corresponding numbers can represent. You should return the results in any order.

The mapping of digits to letters is as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Please note that the input may include non-digit characters, as well as the digits '1' or '0'. These should be disregarded in the processing.

Examples for clarification:

1. For the input "23", the expected output is ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. An empty input, "", should return an empty list: [].
3. The input "2" should yield the output ["a", "b", "c"].
4. For the input "12*30", the expected output is again ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Constraints to consider:

- The length of the input digits can range from 0 to 4.
- Each character in digits should be a number within the range ['2', '9'].

The function signature is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
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