"""You’ve got a string packed with digits from 2 to 9, and your job is to whip up all possible letter combos these numbers could spit out. Yeah, that’s right, just like how you used to punch in numbers on those ancient phone keypads. 

Here’s the lowdown on the digits and their corresponding letters:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Oh, and if you see any non-digit junk, like ones or zeros, toss that garbage right out. 

Here are some pathetic examples to guide you:

Input: digits = "23"  
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""  
Output: []

Input: digits = "2"  
Output: ["a","b","c"]

Input: digits = "12*30"  
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

And just to keep things crystal clear, your digits length should be between 0 and 4, and they must be good ol' digits from '2' to '9'.

Now, the function you need to crank out is: letterCombinations(digits: str) -> list[str]"""

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
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    combinations = []
    backtrack(0, "")
    return combinations