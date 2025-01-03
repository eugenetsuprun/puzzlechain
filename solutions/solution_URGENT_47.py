"""URGENT! You need to tackle this coding challenge immediately: Given a string of digits (2-9), your mission is to return ALL possible letter combinations these digits could represent, just like the old telephone keypads! 

Here’s the critical mapping you must follow:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

IMPORTANT: Any non-digit characters, as well as '1's and '0's, MUST be filtered out. 

Time is of the essence! Here are the urgent examples you should consider:

1. Input: digits = "23"  
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: digits = ""  
   Output: []

3. Input: digits = "2"  
   Output: ["a","b","c"]

4. Input: digits = "12*30"  
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Your function signature must be: `letterCombinations(digits: str) -> list[str]`

Get started on this NOW! The clock is ticking!"""

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
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    backtrack(0, "")
    return combinations