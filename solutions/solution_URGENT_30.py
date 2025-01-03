"""You need to act fast! Take a string of digits from 2-9 and return all possible letter combinations that those digits could represent, just like on a phone keypad! Filter out any non-digit characters—time is of the essence! 

Here's the mapping you must use:
- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Remember, the input can have non-digit characters, ones, or zeros, so act quickly to filter them out. 

Examples to consider:
1. Input: "23" ➔ Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: "" ➔ Output: []
3. Input: "2" ➔ Output: ["a","b","c"]
4. Input: "12*30" ➔ Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Make sure you stick to the constraints: 0 <= digits.length <= 4, and digits[i] must be between '2' and '9'. 

The function signature is: letterCombinations(digits: str) -> list[str]

Get to work NOW!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    filtered_digits = ''.join(filter(lambda x: x in digit_to_char, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_chars = digit_to_char[filtered_digits[index]]
        for char in possible_chars:
            backtrack(index + 1, path + char)
    
    combinations = []
    backtrack(0, "")
    return combinations