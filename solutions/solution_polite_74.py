"""Would you be so kind as to implement a function that, given a string comprised of digits ranging from 2 to 9, returns all potential letter combinations that these digits could represent? Please note that you may disregard any non-digit characters, as well as any occurrences of '1' or '0'. 

You may refer to the following mapping for digit-to-letter correspondence, similar to that found on telephone keypads:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

For instance, with the input `digits = "23"`, the expected output is `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`. Conversely, an empty input, such as `digits = ""`, should return an empty list. 

The function signature is as follows: `letterCombinations(digits: str) -> list[str]`.

I appreciate your assistance with this task!"""

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
    backtrack(0, "")
    return combinations