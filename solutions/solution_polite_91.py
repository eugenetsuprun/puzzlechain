"""You are kindly invited to solve a coding task related to generating letter combinations based on a given string of digits. The string will consist of digits ranging from 2 to 9, and your goal is to return all possible letter combinations that these digits could represent, in any order.

To assist you, please refer to the following mapping of digits to letters, similar to what you might find on a telephone keypad:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Do note that the input number may include non-digit characters, such as ones or zeros. Kindly filter these out in your solution.

Here are a few examples to illustrate the task:

1. If the input is "23," the expected output would be: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. For an empty input, such as "", the output should simply be an empty list: [].
3. If the input is "2," you would return: ["a", "b", "c"].
4. In the case of input "12*30," please provide the same output as in the first example: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

The function you need to implement is as follows: 

```python
def letterCombinations(digits: str) -> list[str]:
```

Thank you for your attention, and I wish you the best of luck with this coding challenge!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_letters = phone_map.get(digits[index], "")
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    filtered_digits = ''.join(filter(lambda x: x in phone_map, digits))
    backtrack(0, "")
    return combinations