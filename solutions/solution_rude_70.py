"""Alright genius, here's the deal. You’ve got a string filled with digits from 2-9, and your pathetic job is to figure out all the possible letter combos those digits could represent. You know, like how they used to map letters on old-school phones? Yeah, that.

Here are the buttons if you’re too slow to remember:
- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

And don’t even think about including any non-digit junk, zeroes, or ones. Filter that garbage out before you start whining about it.

Examples to help your struggling brain:
1. For "23", you should get: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. For an empty string, just give up and return: []
3. For "2", do the bare minimum and return: ["a","b","c"]
4. If you input "12*30", don't panic; just filter and return: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Oh, and by the way, your digits can only be between 0 to 4 characters long and must be within that '2' to '9' range.

Get to it! The function you need to write is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    filtered_digits = ''.join(filter(lambda x: x in digit_to_letters, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_letters[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations