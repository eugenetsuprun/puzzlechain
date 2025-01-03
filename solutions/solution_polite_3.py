"""You are invited to consider a task that involves generating all possible letter combinations based on a given string of digits, specifically those that range from 2 to 9. Each digit corresponds to a specific set of letters as found on telephone keypads, as outlined below:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input string may include non-digit characters, such as ones or zeros, which should be excluded from your processing.

Here are a few examples to guide your understanding:

1. For the input `digits = "23"`, the output should be `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`.
2. If the input is `digits = ""`, the expected output is an empty list: `[]`.
3. With the input `digits = "2"`, the output should simply be `["a", "b", "c"]`.
4. Lastly, for an input like `digits = "12*30"`, the output should again reflect valid combinations from the digit '2' resulting in `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`.

The constraints you might consider are as follows: the length of the digits can range from 0 to 4, and each character in the input is guaranteed to be a digit within the range of '2' to '9'.

Your function signature should be: `letterCombinations(digits: str) -> list[str]`. Thank you for your attention to this task!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
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