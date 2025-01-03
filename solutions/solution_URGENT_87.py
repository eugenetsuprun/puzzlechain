"""You have an urgent coding challenge that demands your immediate attention! The task is to take a string filled with digits ranging from 2-9 and generate all possible letter combinations that correspond to those numbers, just like the letters on a phone keypad! 

Here’s the critical mapping you need to follow:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Important: The input string may contain non-digit characters, zeros, or ones! Make sure to filter those out before you proceed!

You MUST ensure to handle the following cases:
- Example 1: For input "23", your output should be ["ad","ae","af","bd","be","bf","cd","ce","cf"].
- Example 2: If the input is an empty string "", your output should be [].
- Example 3: For input "2", you should return ["a","b","c"].
- Example 4: If the input is "12*30", the expected output is ["ad","ae","af","bd","be","bf","cd","ce","cf"].

You have been entrusted with this task, and the function signature you need to implement is: `letterCombinations(digits: str) -> list[str]`. There’s no time to waste! Get to coding and solve this immediately!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
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