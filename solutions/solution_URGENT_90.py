"""URGENT: You have an important coding challenge ahead! Given a string of digits from 2-9, your task is to generate ALL possible letter combinations that those digits can represent! 

Remember, these digits correspond to letters similar to how they appear on a telephone keypad:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Be aware—any non-digit characters, including ones or zeros, must be filtered out IMMEDIATELY. 

Your solution must handle various cases, including:

1. Input: “23” should yield Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: "" must return Output: []
3. Input: “2” should result in Output: ["a","b","c"]
4. Input: “12*30” must yield Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

You have a tight constraint to consider:
- 0 <= digits.length <= 4
- Each digit must be in the range ['2', '9'].

Act NOW and implement the function with the signature: letterCombinations(digits: str) -> list[str]. Time is of the essence!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and invalid digits
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