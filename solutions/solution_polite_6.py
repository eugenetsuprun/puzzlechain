"""I would be grateful if you could help me with a coding task. The task involves taking a string that contains digits from 2 to 9, and returning all possible letter combinations that the number may represent, similar to the mappings found on telephone buttons. 

Here’s the mapping for your reference:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input may contain non-digit characters, ones, or zeros, which should be filtered out.

Here are a few examples to illustrate the task:

1. For the input `digits = "23"`, the expected output is `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. If the input is `digits = ""`, the output should simply be `[]`.
3. For the input `digits = "2"`, the output would be `["a","b","c"]`.
4. In the case of `digits = "12*30"`, the output should again be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

The constraints for this task are that the length of `digits` can vary from 0 to 4, and each character in `digits` must be a digit within the range ['2', '9'].

I would appreciate it if you could provide a function signature for this task as well: `letterCombinations(digits: str) -> list[str]`. Thank you very much for your assistance!"""

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