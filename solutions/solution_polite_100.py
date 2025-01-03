"""I would greatly appreciate your assistance in solving a coding challenge. The task involves taking a string that contains digits ranging from 2 to 9 and returning all possible letter combinations that correspond to those digits, similar to the mappings found on telephone buttons. 

Here is the mapping for your reference:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input string may contain non-digit characters, as well as the digits 1 and 0, which should be filtered out.

To illustrate, here are a few examples:

1. For an input of `digits = "23"`, the expected output would be `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`.
2. If the input is `digits = ""`, the output should be an empty list: `[]`.
3. With an input of `digits = "2"`, the output would be `["a", "b", "c"]`.
4. Lastly, for `digits = "12*30"`, the output should again be `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`.

The constraints to keep in mind are that the length of the input string can range from 0 to 4, and each character in the string should be a digit from '2' to '9'.

The function signature for your solution should be: `letterCombinations(digits: str) -> list[str]`. 

Thank you for your attention to this task, and I look forward to your insightful solution!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    filtered_digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = phone_map[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations