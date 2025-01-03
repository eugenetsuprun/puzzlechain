"""Urgent! You must tackle this coding challenge immediately! Given a string of digits from 2-9, your task is to return all possible letter combinations these digits could represent based on the classic telephone button mapping. 

Here’s the mapping you need to apply:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Be vigilant! The input may contain non-digit characters, ones, or zeros—make sure to filter them out before processing. 

Consider these example scenarios to guide your implementation:

1. Input: "23" ➔ Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: "" ➔ Output: []
3. Input: "2" ➔ Output: ["a","b","c"]
4. Input: "12*30" ➔ Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Remember, the constraints are clear: 0 <= digits.length <= 4, and digits[i] must be a digit from '2' to '9'.

The clock is ticking! Your function signature should be: letterCombinations(digits: str) -> list[str] 

Get to it!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and '1' or '0'
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