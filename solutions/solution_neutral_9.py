"""Given a string that contains digits from 2 to 9, your task is to return all possible letter combinations that these digits can represent. The mapping of the digits to letters is as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

The input string may include non-digit characters, as well as the digits 0 and 1, which should be filtered out.

Examples for clarification:

1. For the input "23", the output should be ["ad","ae","af","bd","be","bf","cd","ce","cf"].
2. If the input is an empty string "", the output should be [].
3. For the input "2", the output should be ["a","b","c"].
4. For the input "12*30", the output should again be ["ad","ae","af","bd","be","bf","cd","ce","cf"].

Please note the constraints: the length of the digits string can range from 0 to 4, and each character in the string is guaranteed to be a digit between '2' and '9'.

The function signature is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and digits 0 and 1
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