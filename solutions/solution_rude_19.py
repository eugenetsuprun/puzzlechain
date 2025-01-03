"""Got a string full of digits between 2 and 9? Good for you! Now your job is to spit out all the possible letter combos those numbers could stand for, like some kind of human phonebook. Just remember to ignore any useless junk like non-digits, ones, or zeros. Here’s how the buttons break down:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

If your input is a total flop, like empty or filled with trash, just return an empty list. 

Example or two to get your brain in gear:

1. Input: digits = "23" 
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: digits = "12*30" 
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Keep it simple and stick to the constraints: 0 to 4 digits, and they better be between '2' and '9'. 

Oh, and let’s not forget the function signature: letterCombinations(digits: str) -> list[str]. Now get to it!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits or any(d not in '23456789' for d in digits):
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations