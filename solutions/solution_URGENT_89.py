"""You must act NOW! Your task is to take a string of digits from 2-9 and urgently return ALL possible letter combinations that those numbers can represent! Remember, the mapping is just like on your phone's keypad:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

But wait! If you encounter any non-digit characters, ones, or zeros, you MUST filter them out immediately!

Think fast! Here are some examples to guide you:

- Input: "23" should give you Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
- Input: "" should give you Output: []
- Input: "2" should give you Output: ["a","b","c"]
- Input: "12*30" should give you Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Keep in mind the constraints: 0 <= digits.length <= 4, and digits[i] must be a digit in the range ['2', '9'].

Your function signature must be: letterCombinations(digits: str) -> list[str]

Time is of the essence! Act now and deliver the solution!"""

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