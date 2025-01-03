"""You must act NOW! Given a string that may include digits from 2-9, your task is to urgently return all possible letter combinations those digits could represent! These combinations should be generated based on the classic telephone keypad mapping:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Any non-digit characters, including 1s and 0s, MUST be filtered out IMMEDIATELY! 

Consider these examples to guide your implementation:

- Input: digits = "23" should output ["ad","ae","af","bd","be","bf","cd","ce","cf"]
- Input: digits = "" should output []
- Input: digits = "2" should output ["a","b","c"]
- Input: digits = "12*30" should output ["ad","ae","af","bd","be","bf","cd","ce","cf"]

You have a serious responsibility to follow these constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

Time is of the essence! Implement the function signature: letterCombinations(digits: str) -> list[str]. Get to work NOW!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters
    filtered_digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    if not filtered_digits:
        return []
    
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